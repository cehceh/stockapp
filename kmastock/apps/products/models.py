import random
import os
from django.db import models
from kmastock.utils import unique_slug_generator, get_filename
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from django.shortcuts import redirect

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
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
            new_filename=new_filename, 
            final_filename=final_filename)
    

class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True, is_deleted=False)
    
    def is_deleted(self):
        return self.filter(active=False, is_deleted=True)

    def featured(self):
        return self.filter(featured=True, active=True, is_deleted=False)

    def search(self, query):
        lookups = (Q(title__icontains=query) | 
                  Q(description__icontains=query) |
                  Q(price__icontains=query) |
                  Q(tag__title__icontains=query)
                  )
        return self.filter(lookups).distinct()

    def product_already_exists(self, name):
        return self.filter(name=name).exists()


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

    def product_already_exists(self, name):
        return self.get_queryset().product_already_exists(name=name)

class Product(models.Model):
    user        = models.ForeignKey('accounts.CustomUser', blank=True, null=True, on_delete=models.CASCADE)
    vendor      = models.ForeignKey(Vendor, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Vendor Name')
    category    = models.ForeignKey(Categories, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Category Name')
    stock       = models.ForeignKey(Stock, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Store Name')
    name        = models.CharField(default="", max_length=120)
    barcode     = models.CharField(max_length=120, blank=True, null=True, unique=True)
    # slug            = models.SlugField(blank=True, unique=True)
    originprice = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    price       = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    image       = models.ImageField(upload_to="products", null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    featured    = models.BooleanField(default=False)
    active      = models.BooleanField(default=True)
    is_deleted  = models.BooleanField(default=False) 
    updateduser = models.ForeignKey('accounts.CustomUser', related_name='user_make_product_changes', blank=True, null=True, on_delete=models.CASCADE)
    

    objects = ProductManager()

    def product_edit_url(self):
        return reverse("products:edit_product", kwargs={"id": self.id})

    def __str__(self):
        return '{}'.format(self.name)

    @property
    def title(self):
        return self.name

    def get_downloads(self):
        qs = self.productfile_set.all()
        return qs
