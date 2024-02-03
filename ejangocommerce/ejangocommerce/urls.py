from django.contrib import admin
from django.urls import path

from core.views import frontpage, shop
from product.views import product

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>/', product, name='product'),
    # slug:slug is that we use a dinamic url for each product
    path('admin/', admin.site.urls),
]
