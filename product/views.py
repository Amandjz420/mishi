import requests
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.conf import settings

from elapi.base_views import CreateView, ListView
from .schema import ProductGetApiSchema, OrderApiSchema
from .task import createOrders

class ProductInfoApi(CreateView):

    schema_class = ProductGetApiSchema
    permission_classes = (AllowAny,)
    post_status_code = 200

    def perform_create(self, data):
        url = settings.BASE_URL + \
              'admin/api/2020-07/products/' +\
              str(data['product_id']) + '.json'
        headers = {'Content-type': 'application/json'}
        resp = requests.get(url,  headers=headers)
        return resp.json()


class CreateOrder(CreateView):

    schema_class = OrderApiSchema
    permission_classes = (AllowAny,)
    post_status_code = 200

    def perform_create(self, data):
        createOrders(data['orders'])
        return {'status': 'orders created'}




