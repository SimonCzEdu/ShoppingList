from django.db import models
from django.contrib.auth.models import User

PRIORITY = ((0, "Needed"), (1, "Will need soon"), (2, "Would be nice to have"), (3, "It can wait"))

# Create your models here.
class List(models.Model):
    list_name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="shopping_list")
    
    def __str__(self):
        return f"{self.list_name}"

class Item(models.Model):
    list = models.ForeignKey(
        List, on_delete=models.CASCADE, related_name="items"
    )
    item_name = models.CharField(max_length=200, unique=False)
    min_quantity = models.IntegerField(default=0, blank=False)
    current_quantity = models.IntegerField(default=0, blank=False)
    priority = models.IntegerField(choices=PRIORITY, default=0)
    item_price = models.DecimalField(default=0, max_digits=6, decimal_places=2, blank=False)

    class Meta:
        ordering = ['-list', 'item_name',]

    def __str__(self):
        return f"{self.item_name}"