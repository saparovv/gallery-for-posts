from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='product_list'),
    path('<int:pk>/', views.details, name='product_detail'),
    path('<int:pk>/edit/', views.edit_product, name='edit_product'),
    path('<int:pk>/delete/', views.delete_product, name='delete'),
]