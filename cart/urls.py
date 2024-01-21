from django.urls import path

from .views import AddInCartView, RemoveFromCartView, ClearCartView

app_name = 'cart'

urlpatterns = [
    path('add/<int:pk>/', AddInCartView.as_view(), name='add_in_cart'),
    path('remove/<int:pk>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('clear/', ClearCartView.as_view(), name='clear_cart'),
]
