from django.db import models

# Create your models here.
class Brand(models.Model):
    brand_name=models.CharField(max_length=15)
    slug=models.SlugField(max_length=100,default="",null=True,blank=True,unique=True)
    def __str__(self):
        return self.brand_name