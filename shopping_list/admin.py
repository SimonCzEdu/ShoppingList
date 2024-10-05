from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import List, Item


@admin.register(List)
class ListAdmin(SummernoteModelAdmin):

    list_display = ('list_name', 'slug', 'author')
    search_fields = ['list_name']
    list_filter = ('author',)
    prepopulated_fields = {'slug': ('list_name',)}

@admin.register(Item)
class ItemAdmin(SummernoteModelAdmin):

    list_display = ('item_name', 'list', 'priority', 'item_price')
    search_fields = ['priority', 'item_name', 'item_price']
    list_filter = ('priority', 'item_name', 'item_price')

# Register your models here.
