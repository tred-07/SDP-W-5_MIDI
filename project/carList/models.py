from django.db import models
from django.contrib.auth.models import User
from brand.models import Brand
# Create your models here.
class CarList(models.Model):
    image=models.ImageField(upload_to='uploads/')
    name=models.CharField(max_length=40)
    price=models.IntegerField()
    brand_name=models.ForeignKey(Brand,on_delete=models.CASCADE)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)