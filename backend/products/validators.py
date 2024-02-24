from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Product

# can create validators for models or model forms


# def validate_title(value):
#     # iexact is case insensitive
#     qs = Product.objects.filter(title__iexact=value)
#     if qs.exists():
#         raise serializer.ValidationError("This title exists")
#     return value


def validate_title_no_hello(value):
    if "hello" in value.lower():
        raise serializer.ValidationError("hello is not allowed")
    return value


unique_product_title = UniqueValidator(queryset=Product.objects.all())
