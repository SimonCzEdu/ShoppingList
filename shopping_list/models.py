from django.db import models
from django.contrib.auth.models import User

PRIORITY = ((0, "Select Priority"), (1, "Needed"), (2, "Will need soon"), (3, "Would be nice to have"), (4, "It can wait"))

# Create your models here.
class List(models.Model):
    list_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="shopping_lists")
    
    def __str__(self):
        return f"{self.list_name}"

class Item(models.Model):
    list = models.ForeignKey(
        List, on_delete=models.CASCADE, related_name="items"
    )
    item_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    min_quantity = models.IntegerField(default=0, blank=True)
    current_quantity = models.IntegerField(default=0, blank=True)
    priority = models.IntegerField(choices=PRIORITY, default=0)
    item_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True)

    def __str__(self):
        return f"{self.item_name}"
