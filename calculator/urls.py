from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),   
    path('create/', views.create_product, name='create_product'), 
    path('update/', views.update_product, name='update_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product') ,
    path('product/<int:product_id>/', views.get_product, name='get_product'),
]