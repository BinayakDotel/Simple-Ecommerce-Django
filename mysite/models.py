from django.db import models

class Category(models.Model):
    category= models.CharField(max_length=255)
    category_id= models.AutoField(primary_key=True)

class Product(models.Model):
    product_id= models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    price= models.FloatField()  
    c_id= models.ForeignKey(Category, on_delete=models.CASCADE)
    