from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class book(models.Model):
    bookname=models.CharField(max_length=50,default=1,primary_key=True)
    price=models.IntegerField(default=1)
    image=models.ImageField(blank=True)
    def __str__(self):
        return self.bookname
class ordereditems(models.Model):
    username=models.CharField(max_length=50,default=1)
    bookname1=models.CharField(max_length=50,default=1)
    price = models.CharField(max_length=50,default=1)
    quantity=models.CharField(default=1,max_length=50)
    def __str__(self):
        return self.username
class MyCart(models.Model):
    username=models.CharField(max_length=50)
    bookname1=models.CharField(max_length=50,default=1)
    price=models.IntegerField(blank=True)
    quantity=models.IntegerField(default=1)
    def __str__(self):
        return self.bookname1
class pendingitems(models.Model):
    username=models.CharField(max_length=50,default=1)
    bookname1=models.CharField(max_length=50,default=1)
    price = models.CharField(max_length=50,default=1)
    quantity=models.CharField(default=1,max_length=50)
    def __str__(self):
        return self.username

