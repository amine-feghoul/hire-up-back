from django.http import request, HttpResponse, JsonResponse
from django.http.response import Http404, HttpResponseForbidden, HttpResponseNotAllowed
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from profiles.models import RecruiterProfile
from profiles.serializers import CompanySerializer, RecruiterSerializer
from .serializers import ApplicationsSerializer,readApplicationsSerializer
from .models import applications
from offers.models import offer
from profiles.models import profileModel,authorizedViewers
from profiles.serializers import appProfileSerializer
from offers.serializers import OffersSerializer
from authapp.models import userAccount
# Create your views here.


@csrf_exempt
@api_view(['GET','POST','DELETE'])
@permission_classes([IsAuthenticated])
def applicationsList(request):   
    if request.method == 'GET':
        try:
            if(str(request.user.get_user_type()) == "employer"):
                data = applications.objects.all().filter(employer_id = request.user.id)
                result = []
                for i in data:
                    profile = profileModel.objects.get(user_id = i.candidate.id)           
                    profileSerialize = appProfileSerializer(profile)
                    offerItem = offer.objects.get(id = i.offer.id)
                    offerSerializer = OffersSerializer(offerItem)
                    applicationSerialize = ApplicationsSerializer(i)
                    result.append({"application": applicationSerialize.data,"offer" : offerSerializer.data , "candidate":profileSerialize.data})
            elif(str(request.user.get_user_type()) == "candidate"):
                profile = profileModel.objects.get(user_id = int(request.user.get_id()))           
                data = applications.objects.all().filter(condidate_id = int(profile.id))
                result = []
                for i in data:
                    offerItem = offer.objects.get(id = i.offer_id.get_id())
                    offerSerializer = OffersSerializer(offerItem)
                    company = RecruiterProfile.objects.get(user = i.employer)
                    companySerializer = CompanySerializer(company)
                    applicationSerialize = ApplicationsSerializer(i)
                    result.append({"application": applicationSerialize.data,"offer" : offerSerializer.data , "company":companySerializer.data})
            return JsonResponse({"applications" : result}, safe=False)
        except Exception as e:
            # print(e)
            return JsonResponse({"applications" : "error"}, status=500, safe=False)

    elif request.method == 'POST':
        if(str(request.user.get_user_type()) == "candidate"):
            data = JSONParser().parse(request) 
            # print(data)    
            offer_data = offer.objects.get(id = int(data['offer_id']))  
            data['employer_id'] = offer_data.userId_id
            profile = profileModel.objects.get(user_id = int(request.user.get_id()))
            data['condidate_id'] = profile.id
            data['state'] = "on_hold"
            if (applications.objects.filter(offer_id = data["offer_id"],condidate_id =data["condidate_id"] ).exists()):
                return JsonResponse({"msg":"already applied to this offer"}, status=400)
            serializer = ApplicationsSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)

        else:
            message ={}
            message["msg"] = "u have to be condidate in order to do this function"
            return JsonResponse(message,status = 404)
@csrf_exempt
@api_view(['GET','DELETE'])
@permission_classes([IsAuthenticated])
def applicationsItem(request,pk):   
    if request.method == 'GET':
        application = applications.objects.get(id = pk)
        serializer = ApplicationsSerializer(data = application)
        if serializer.is_valid():
            return JsonResponse(serializer.data,status = 200)
        else:
            return JsonResponse(serializer.errors,status = 500)
    elif request.method == 'DELETE':
        application = applications.objects.get(id = pk)
        if( request.user.get_id() == application.condidate_id_id):
            application.delete()
            return JsonResponse({"deleted":True}, status=200)
        else :
            msg={"Unauthorized":"you have no access to the data"}
            return JsonResponse(msg,status=401)
