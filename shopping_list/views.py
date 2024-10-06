from django.shortcuts import render, get_object_or_404,reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
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


def item_edit(request, slug, item_id):
    """
    view to edit items
    """
    if request.method == "POST":

        queryset = List.objects.all()
        list = get_object_or_404(queryset, slug=slug)
        item = get_object_or_404(Item, pk=item_id)
        item_form = ItemForm(data=request.POST, instance=item)

        if item_form.is_valid():
            item = item_form.save(commit=False)
            item.list = list
            item.save()
            messages.add_message(request, messages.SUCCESS, 'Item Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating item!')

    return HttpResponseRedirect(reverse('list_detail', args=[slug]))


def item_delete(request, slug, item_id):
    """
    view to delete item
    """
    queryset = List.objects.all()
    list = get_object_or_404(queryset, slug=slug)
    item = get_object_or_404(Item, pk=item_id)

    item.delete()
    messages.add_message(request, messages.SUCCESS, 'Item deleted!')
    
    return HttpResponseRedirect(reverse('list_detail', args=[slug]))