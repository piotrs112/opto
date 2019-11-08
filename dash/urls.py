from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('client/<int:pk>/', views.ClientDetail.as_view(), name='client'),
    path('client/', views.ClientList.as_view(), name='client_list'),
    path('client/new/', views.ClientCreate.as_view(), name='client_create'),
    path('order/<int:pk>/', views.OrderDetail.as_view(), name='order'),
    path('order/', views.OrderList.as_view(), name='order_list'),
    path('order/new/', views.OrderCreate.as_view(), name='order_create'),
]