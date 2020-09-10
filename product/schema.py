from marshmallow import post_load, validates

from elapi.base_schema import Schema
from elapi.fields import fields
from elapi.exceptions import InvalidDataException


class ProductGetApiSchema(Schema):

    product_id = fields.Integer(required=True)


class OrderSchema(Schema):

    id = fields.Integer(required=True)
    quant = fields.Integer(required=True)


class OrderApiSchema(Schema):

    orders = fields.Nested(OrderSchema, many=True)