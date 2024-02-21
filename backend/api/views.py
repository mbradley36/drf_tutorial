import json
from django.forms.models import model_to_dict
from django.http import JsonResponse
from products.models import Product


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
