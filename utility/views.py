from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import numpy

# Create your views here.


@csrf_exempt
def sum(request):
    if request.method == 'POST':
        req_json = json.loads(request.body)
        numbers = req_json.get('numbers')

        return JsonResponse({
            'result': sum(numbers)
        })
    return JsonResponse({
        'error': 'POST request required'
    })


@csrf_exempt
def avg(request):
    if request.method == 'POST':
        req_json = json.loads(request.body)
        numbers = req_json.get('numbers')

        return JsonResponse({
            'result': numpy.average(numbers)
        })
    return JsonResponse({
        'error': 'POST request required'
    })


@csrf_exempt
def product(request):
    if request.method == 'POST':
        req_json = json.loads(request.body)
        numbers = req_json.get('numbers')

        return JsonResponse({
            'result': numpy.prod(numbers)
        })
    return JsonResponse({
        'error': 'POST request required'
    })
