from django.db import models
from django.db.models import Q
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class ClientQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)
    # def featured(self):
    #     return self.filter(featured=True, active=True)

    def search(self, query):
        lookups = (Q(name__icontains=query) | 
                  Q(description__icontains=query) 
                #   Q(price__icontains=query) |
                #   Q(tag__title__icontains=query)
                  )
        return self.filter(lookups).distinct()

class ClientManager(models.Manager):
    def get_queryset(self):
        return CategoriesQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    # def featured(self): #Vendor.objects.featured() 
    #     return self.get_queryset().featured()

    def get_vendor_by_id(self, id):
        qs = self.get_queryset().filter(id=id) # Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().active().search(query)


class Client(models.Model):
    user        = models.ForeignKey('accounts.CustomUser', blank=True, null=True, on_delete=models.CASCADE)
    name        = models.CharField(max_length=100)
    phone       = PhoneNumberField(blank=True, null=True)
    mobile      = PhoneNumberField(blank=True, null=True)
    address     = models.CharField(max_length=150, blank=True, null=True)
    email       = models.EmailField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now_add=True)
    active      = models.BooleanField(default=True)
    featured    = models.BooleanField(default=False)
    is_deleted  = models.BooleanField(default=False) # User Library


    objects = ClientManager()

    def get_absolute_url(self):
        #return "/products/{slug}/".format(slug=self.slug)
        return reverse("clients:detail", kwargs={"id": self.id})


    def __str__(self):
        return '{}'.format(self.name)