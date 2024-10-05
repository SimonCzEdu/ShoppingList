from django.shortcuts import render
from django.views import generic
from .models import List

# Create your views here.
class ListsOfList(generic.ListView):
    queryset = List.objects.all()
    template_name = "lists_list.html"