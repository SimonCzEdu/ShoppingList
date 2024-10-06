from .models import Item
from django import forms


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('item_name','min_quantity', 'current_quantity', 'priority', 'item_price')