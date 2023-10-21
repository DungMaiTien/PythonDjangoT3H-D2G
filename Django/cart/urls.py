from django.urls import path

from . import views

app_name = "cart"
urlpatterns = [
    path('', views.cart, name = "cart"),
    path('delete/<int:cart_item_id>/', views.delete_cart_item, name='delete_cart_item'),

]
