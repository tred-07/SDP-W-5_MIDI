from django.db import models
from car.models import Car
# Create your models here.

class Comment(models.Model):
    car=models.ForeignKey(Car,on_delete=models.CASCADE,related_name='comment')
    name=models.CharField(max_length=40)
    email=models.EmailField(unique=True,blank=False,null=False)
    commentDes=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Commented by: {self.name} , on: {self.car}'