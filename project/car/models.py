from django.db import models
from brand.models import Brand
# Create your models here.
class Car(models.Model):
    image=models.ImageField(upload_to='uploads/')
    name=models.CharField(max_length=40)
    description=models.CharField(max_length=150)
    quantity=models.IntegerField()
    price=models.IntegerField()
    brand_name=models.ForeignKey(Brand,on_delete=models.CASCADE)
    slug=models.SlugField(max_length=40,unique=True)

    def __str__(self):
        return self.name