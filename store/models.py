from django.db import models
from category.models import category
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    product_name    = models.CharField(max_length=50, unique=True)
    slug            = models.SlugField(max_length=100, unique=True)
    description     = models.TextField(max_length=255)
    price           = models.IntegerField()
    images          = models.ImageField(upload_to='photos/products')
    stock           = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    category        = models.ForeignKey('category.category', on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name        = 'product'
        verbose_name_plural = 'products'
        
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
        
    def __str__(self):
        return str(self.product_name)