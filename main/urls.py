from django.urls import path

from .views import HomeView, ShopView, ProductDetails, CartView, CheckoutView

app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('detail/<int:pk>/', ProductDetails.as_view(), name='detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
]
