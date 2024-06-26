from django.urls import path 

from cart.views import add_to_cart, cart, checkout, hx_menu_cart, update_cart

urlpatterns = [
    path('', cart, name='cart'),
    path('checkout', checkout, name='checkout'),
    # slug:slug is that we use a dinamic url for each product
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('update_cart/<int:product_id>/<str:action>', update_cart, name='update_cart'),
    path('hx_menu_cart/', hx_menu_cart, name="hx_menu_cart"),
]
