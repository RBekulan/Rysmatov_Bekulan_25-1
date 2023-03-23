from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Products(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='products')


class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='reviews')
