import json
from django.http import JsonResponse


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
