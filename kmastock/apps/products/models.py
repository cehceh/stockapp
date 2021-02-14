import random
import os
from django.db import models
from kmastock.utils import unique_slug_generator, get_filename
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.urls import reverse

from apps.vendors.models import Vendor
from apps.stocks.models import Stock
from apps.category.models import Categories

from django.contrib.auth import get_user_model
User = get_user_model()
# import get_user_model
# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    # print(instance)
    #print(filename)
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
            new_filename=new_filename, 
            final_filename=final_filename
            )

class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)

    def search(self, query):
        lookups = (Q(title__icontains=query) | 
                  Q(description__icontains=query) |
                  Q(price__icontains=query) |
                  Q(tag__title__icontains=query)
                  )
        # tshirt, t-shirt, t shirt, red, green, blue,
        return self.filter(lookups).distinct()

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self): #Product.objects.featured() 
        return self.get_queryset().featured()

    def get_product_by_id(self, id):
        qs = self.get_queryset().filter(id=id) # Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().active().search(query)


class Product(models.Model):
    user            = models.ForeignKey('accounts.CustomUser', blank=True, null=True, on_delete=models.CASCADE)
    vendor          = models.ForeignKey(Vendor, blank=True, null=True, on_delete=models.CASCADE)
    category        = models.ForeignKey(Categories, blank=True, null=True, on_delete=models.CASCADE)
    stock           = models.ForeignKey(Stock, blank=True, null=True, on_delete=models.CASCADE)
    title           = models.CharField(max_length=120)
    # slug            = models.SlugField(blank=True, unique=True)
    description     = models.TextField(blank=True, null=True)
    price           = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    image           = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured        = models.BooleanField(default=False)
    active          = models.BooleanField(default=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now_add=True)
    is_deleted      = models.BooleanField(default=False) # User Library

    objects = ProductManager()

    def get_absolute_url(self):
        #return "/products/{slug}/".format(slug=self.slug)
        return reverse("products:detail", kwargs={"id": self.id})


    def __str__(self):
        return '{}'.format(self.title)

    @property
    def name(self):
        return self.title

    def get_downloads(self):
        qs = self.productfile_set.all()
        return qs
