import requests

from celery import shared_task
from django.conf import settings


@shared_task
def createOrders(data):
    url = settings.BASE_URL + \
          'admin/api/2020-07/orders.json'
    headers = {'Content-type': 'application/json'}
    formData = {
      "order": {
        "line_items": []
      }
    }
    for obj in data:
        formData['order']['line_items'].append(
            {"variant_id": obj['id'], "quantity": obj['quant']}
        )
    resp = requests.post(url, json=formData, headers=headers)
    decreaseInventory(resp, data)


@shared_task
def decreaseInventory(data):
    """api to update the inventory but missing inventory location id"""
    pass

