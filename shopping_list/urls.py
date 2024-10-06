from . import views
from django.urls import path

urlpatterns = [
    path('', views.ListsOfList.as_view(), name='home'),
    path( '<slug:slug>/', views.list_detail, name='list_detail'),
    path( '<slug:slug>/edit_item/<int:item_id>',
        views.item_edit, name='item_edit'),
    path('<slug:slug>/delete_item<int:item_id>',
        views.item_delete, name='item_delete'),
]