from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.db import models

from category.models import Category


class Product(models.Model):
    title = models.CharField(unique=True)
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    session_keys = models.ManyToManyField(
        Session, related_name="products", blank=True, through="SearchHistory"
    )

    def __str__(self):
        return self.title


class SearchHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
