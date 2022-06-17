from django.http import request, HttpResponse, JsonResponse
from django.http.response import Http404, HttpResponseForbidden, HttpResponseNotAllowed
import profiles
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import CategorySerializer, OffersSerializer,OfferSkillsSerializer,SkillSerializer
from .models import offer, offerCategorie,offerSkills,Skill
from profiles.serializers import CompanySerializer
from profiles.models import RecruiterProfile

# Create your views here.
MAX_OFFERS_PERPAGE = 10
@csrf_exempt
@api_view(['GET',"POST"])
@permission_classes([IsAuthenticated])
def offersList(request):
    if request.method == 'GET':
 
        # print(request.query_params)
        data = request.query_params.dict()
        # print(data)
        offerPerPage = int(data["offerPerPage"])
        if(type(offerPerPage) is not int ):
            return JsonResponse({"msg":"offerPerPage must be int"},status = 400, safe=False)
        page = int(data['page'])
        if(page < 0):
            return JsonResponse({"msg":"offerPerPage must be positive"},status = 400, safe=False)
        
        if(offerPerPage > MAX_OFFERS_PERPAGE):
            # print("got excceding number")
            offerPerPage = MAX_OFFERS_PERPAGE
        try:
            offers = offer.objects.all()[page*offerPerPage:offerPerPage*(page +1)]
            serializer = OffersSerializer(offers, many=True)    
            # print(serializer.data)
            result = []
            # ids = [i.id for i in offers ]
            for k,i in enumerate(offers):

                temp = {
                    "offer":serializer.data[k]
                }
                
                company = RecruiterProfile.objects.get(id = i.companyProfile.get_id())
                companySerializer = CompanySerializer(company)
                temp["company"] = companySerializer.data
                result.append(temp)
            return JsonResponse({"offers":result}, safe=False)
        except : 
            return JsonResponse({"offers":[]}, status= 404 , safe=False)
    elif request.method == 'POST':
        if(str(request.user.get_user_type()) == "employer"):
            data = JSONParser().parse(request)    
                
            data['userId' ]=request.user.id
            result = ""
            data["companyProfile" ]=RecruiterProfile.objects.get(user = request.user.get_id()).get_id()            
            data["category"] = data["offerCategory"]["label"] 
            data["contractType"] = data["contractType"]["label"] 
            # skills = [i["label"] for i in data["skills"]]
            skills = data["skills"]
            data.pop("skills")
            # print(data)
            serializer = OffersSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                for i in skills:  
                    skill = Skill.objects.get(label=i)
                    currentOffer = offer.objects.get(id=serializer.data['id'])
                    temp = offerSkills(label = skill,offer_id =currentOffer)
                    temp.save()          

                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
        else:
            message ={}
            message["msg"] = "u have to be employer in order to do this function"
            return JsonResponse(message,status = 404)
@csrf_exempt
@api_view(['GET','POST','DELETE','PUT'])
@permission_classes([IsAuthenticated])
def offerItem(request,pk=None):
    offers = offer.objects.get(id = pk)   
    if request.method == 'GET':
            serializer = OffersSerializer(offers)   
            skills = offerSkills.objects.filter(offer_id = offers.get_id())
            skillSerializer = OfferSkillsSerializer(data=skills,many=True)
            skillSerializer.is_valid()
            recruiter = RecruiterProfile.objects.get(user_id = serializer.data["userId"])
            companySerialzer = CompanySerializer(recruiter)
            return JsonResponse ({"offer":serializer.data,"company":companySerialzer.data,"skills":skillSerializer.data}, safe=False)
    
    elif request.method =="PUT":
        if(str(request.user.get_user_type()) == "employer" and str(offers.userId) == str(request.user.get_email())):
            data = JSONParser().parse(request)  
            data['userId' ]=request.user.id       
            serializer = OffersSerializer(offers,data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            return JsonResponse(serializer.errors, status=400)
        message = {"msg":"not authorized to do this function"}
        return JsonResponse(message,status= 400)
    
    elif request.method == 'DELETE':
        if(offers.userId.get_email() == request.user.email):
            offers.delete()
            return HttpResponse(status=200)
        return HttpResponse(status = 301)

def compareEmails(email1,email2):
    for i,k in enumerate(email1):
        # print(i,k)
        pass


@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getSkills(request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills,many=True)
        return JsonResponse(serializer.data,safe=False  , status=200)

@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def offerCategoriesList(request):
    types = offerCategorie.objects.all()
    serializer = CategorySerializer(types,many = True)
    return JsonResponse(serializer.data,status = 200 ,safe=False)