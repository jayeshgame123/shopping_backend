from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .views import ProductView,CartView,CartItemsView,UserView,OrderView,OrderItemsView

urlpatterns = [
    path('product/', ProductView.as_view()),
    path('product/<int:pk>/', ProductView.as_view()),

    path('cart/', CartView.as_view()),
    path('cart/<int:pk>/', CartView.as_view()),

    path('cartitems/', CartItemsView.as_view()),
    path('cartitems/<cartId>/', CartItemsView.as_view()),
    path('cartitems/delete/<int:pk>/', CartItemsView.as_view()),

    path('user/', UserView.as_view()),
    path('user/<int:pk>/',UserView.as_view()),

    path('order/', OrderView.as_view()),
    path('order/<int:pk>/',OrderView.as_view()),

    path('orderitems/', OrderItemsView.as_view()),
    path('orderitems/<int:pk>/',OrderItemsView.as_view())

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)