from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views
from django.conf.urls.static import static
from django.urls import path

from cart.views import add_to_cart, cart
from core.views import frontpage, shop, signup
from product.views import product

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>/', product, name='product'),
    path('cart/', cart, name='cart'),
    # slug:slug is that we use a dinamic url for each product
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #with changes on db module and this line, able to use media files
