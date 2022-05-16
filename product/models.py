from ast import keyword
from email.mime import image
from pyexpat import model
from re import S, T
from telnetlib import STATUS
from turtle import update
from unicodedata import category
from venv import create
from django.db import models

# Create your models here.

class Category(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    parent = models.ForeignKey('self',blank=True, null=True,related_name='children',on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to = "images/")
    status = models.CharField(max_length=10,choices=STATUS)
    slug = models.SlugField(unique=True)
    create_at  = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    #Specify verbose_name
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Product(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),

    )

    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank = True, upload_to = 'images/')
    price = models.FloatField()
    discount = models.CharField(max_length=10,choices=STATUS,default=False)
    discount_percent = models.FloatField(null=True,default=0)
    amount = models.IntegerField()
    details = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at =models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title