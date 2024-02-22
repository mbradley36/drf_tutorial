import json
from django.forms.models import model_to_dict
from django.http import JsonResponse
from products.models import Product
from products.serializers import ProductSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response


def api_home(request, *args, **kwargs):
    # request.GET can be used to get query params
    body = request.body  # byte stream of json data
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print(data.keys())
    data['headers'] = dict(request.headers)
    # should be in headers, but can also access directly
    data['content_type'] = request.content_type
    return JsonResponse({"message": "hiiii"})


def usesModels(request, *args, **kwargs):
    # basic serialization:
    # model instance
    # turn into a Pthon dict
    # return JSON to client
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title'])
    return JsonResponse(data)

# the django-only way of defining calls would be:
# if request.method != "POST":
#   return Response({"detail": "GET NOT ALLLOWED"}, status=405)


@api_view(["GET"])
def drf_view(request, *arts, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data = model_to_dict(model_data, fields=['id', 'title', 'sale_price'])
        data = ProductSerializer(instance).data
    return Response(data)


@api_view(["POST"])
def drf_post_view(request, *arts, **kwargs):
    serializer = ProductSerializer(data=request.data)
    # can pass serializer.is_valid(raise_exception=True) to get better error messaging
    if (serializer.is_valid()):
        # instance = serializer.save()
        # print(instance)
        return Response(serializer.data)
    return Response()
