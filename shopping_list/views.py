from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import List

# Create your views here.
class ListsOfList(generic.ListView):
    queryset = List.objects.all()
    template_name = "shopping_list/index.html"
    paginate_by = 100

def list_detail(request, slug):

    queryset = List.objects.filter(slug=slug)
    list = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "shopping_list/list_detail.html",
        {"list": list},
    )