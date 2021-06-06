from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.utils.timezone import now

# Create your models here.

class CategoriesQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)
    # def featured(self):
    #     return self.filter(featured=True, active=True)
    def category_already_exists(self, name):
        return self.filter(name=name).exists()

    def search(self, query):
        lookups = (Q(name__icontains=query) | 
                    Q(description__icontains=query) 
                #   Q(price__icontains=query) |
                #   Q(tag__title__icontains=query)
                )
        return self.filter(lookups).distinct()

class CategoriesManager(models.Manager):
    def get_queryset(self):
        return CategoriesQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    # def featured(self): #Vendor.objects.featured() 
    #     return self.get_queryset().featured()

    def get_category_by_id(self, id):
        qs = self.get_queryset().filter(id=id) # Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().active().search(query)


class Categories(models.Model):
    user        = models.ForeignKey('accounts.CustomUser', blank=True, null=True, on_delete=models.CASCADE)
    name        = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True) # To get the updated date 
    active      = models.BooleanField(default=True)
    featured    = models.BooleanField(default=False)
    is_deleted  = models.BooleanField(default=False) 
    updateduser = models.ForeignKey('accounts.CustomUser', related_name='user_make_category_changes', blank=True, null=True, on_delete=models.CASCADE)


    objects = CategoriesManager()

    # def get_absolute_url(self):
    #     #return "/products/{slug}/".format(slug=self.slug)
    #     return reverse("category:detail", kwargs={"id": self.id})


    def __str__(self):
        return '{}'.format(self.name)