from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import numpy

# Create your views here.


@csrf_exempt
def sum(request):
    req_json = json.loads(request.body)
    numbers = req_json.get('numbers')

    return JsonResponse({
        'result': sum(numbers)
    })


@csrf_exempt
def avg(request):
    req_json = json.loads(request.body)
    numbers = req_json.get('numbers')

    return JsonResponse({
        'result': numpy.average(numbers)
    })


@csrf_exempt
def product(request):
    req_json = json.loads(request.body)
    numbers = req_json.get('numbers')

    return JsonResponse({
        'result': numpy.prod(numbers)
    })
