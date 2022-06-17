from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.http import request, HttpResponse, JsonResponse

from .serializers import *
from .models import *
# Create your views here.

@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def PostionsList(request):
    types = Position.objects.all()
    serializer = PositionSerializer(types,many = True)
    return JsonResponse(serializer.data,status = 200 ,safe=False)

@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def CompanyTypesList(request):
    types = companyType.objects.all()
    serializer = CompanyTypeSerializer(types,many = True)
    return JsonResponse(serializer.data,status = 200 ,safe=False)

@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def SectorsList(request):
    types = Sector.objects.all()
    serializer = SectorSerializer(types,many = True)
    return JsonResponse(serializer.data,status = 200 ,safe=False)

@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def OfferTypesList(request):
    types = offerType.objects.all()
    serializer = OfferTypeSerializer(types,many = True)
    return JsonResponse(serializer.data,status = 200 ,safe=False)

@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def SkillsList(request):
    types = Skill.objects.all()
    serializer = SkillSerializer(types,many = True)
    return JsonResponse(serializer.data,status = 200 ,safe=False)

@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ContractTypesList(request):
    types = contractType.objects.all()
    serializer = ContractTypeSerializer(types,many = True)
    return JsonResponse(serializer.data,status = 200 ,safe=False)



@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def InstitutesList(request):
    types = Institute.objects.all()
    serializer = InstituteSerializer(types,many = True)
    return JsonResponse(serializer.data,status = 200 ,safe=False)

@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def DegreesList(request):
    types = Degree.objects.all()
    serializer = DegreeSerializer(types,many = True)
    return JsonResponse(serializer.data,status = 200 ,safe=False)


@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def LanguagesList(request):
    types = Language.objects.all()
    serializer = LanguageSerializer(types,many = True)
    return JsonResponse(serializer.data,status = 200 ,safe=False)


@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def SitesList(request):
    types = Site.objects.all()
    serializer = SiteSerializer(types,many = True)
    return JsonResponse(serializer.data,status = 200 ,safe=False)

@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def StudyFieldsList(request):
    types = studyField.objects.all()
    serializer = StudyFieldSerializer(types,many = True)
    return JsonResponse(serializer.data,status = 200 ,safe=False)