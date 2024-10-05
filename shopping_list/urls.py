from . import views
from django.urls import path

urlpatterns = [
    path('', views.ListsOfList.as_view(), name='home'),
    path('<slug:slug>/', views.list_detail, name='list_detail'),
]