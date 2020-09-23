from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .serializers import BlendSerializer

@csrf_exempt
def rendering(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        blendParam = BlendSerializer(data=data)
        if(blendParam.is_valid() == False):
            return JsonResponse(blendParam.errors, status=400)
        else:
            print(blender)
            return JsonResponse(blendParam.data, status=201)
    
