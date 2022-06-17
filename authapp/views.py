from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from authapp.serializers import userTypesSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
