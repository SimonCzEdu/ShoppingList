from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import List, Item
from .forms import ItemForm

# Create your views here.

class ListsOfList(generic.ListView):
    queryset = List.objects.all()
    template_name = "shopping_list/index.html"
    paginate_by = 100


def list_detail(request, slug):

    queryset = List.objects.filter(slug=slug)
    list = get_object_or_404(queryset, slug=slug)
    items = Item.objects.filter(list=list)
    items_count = items.all().count()
    item_form = ItemForm
    if request.method == "POST":
        item_form = ItemForm(data=request.POST)
        if item_form.is_valid():
            item = item_form.save(commit=False)
            item.author = request.user
            item.list = list
            item.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Item added'
    )

    return render(
        request,
        "shopping_list/list_detail.html",
        {
            "list": list,
            "items": items,
            "items_count": items_count,
            "item_form": item_form,
        },
    )