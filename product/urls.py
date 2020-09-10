from django.conf.urls import url

from . import views

app_name = 'product'
urlpatterns = [
    url(r'^info/$', views.ProductInfoApi.as_view(), name='product_info'),
    url(r'^create-order/$', views.CreateOrder.as_view(), name='product_info'),
]