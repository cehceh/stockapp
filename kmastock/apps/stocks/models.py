from django.db import models
from django.db.models import Q
from django.urls import reverse

# Create your models here.

class StockQuerySet(models.query.QuerySet):
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

class StockManager(models.Manager):
    def get_queryset(self):
        return StockQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    # def featured(self): #Vendor.objects.featured() 
    #     return self.get_queryset().featured()

    def get_stock_by_id(self, id):
        qs = self.get_queryset().filter(id=id) # Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().active().search(query)

class Stock(models.Model):
    user        = models.ForeignKey('accounts.CustomUser', blank=True, null=True, on_delete=models.CASCADE)
    name        = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    active      = models.BooleanField(default=True)
    featured    = models.BooleanField(default=False)
    is_deleted  = models.BooleanField(default=False) # 
    updateduser = models.ForeignKey('accounts.CustomUser', related_name='user_make_stock_changes', blank=True, null=True, on_delete=models.CASCADE)

    objects = StockManager()

    def get_absolute_url(self):
        return reverse("stocks:edit_stock", kwargs={"id": self.id})


    def __str__(self):
        return '{}'.format(self.name)
