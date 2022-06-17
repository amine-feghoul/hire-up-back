from django.http import request, HttpResponse, JsonResponse
from django.http.response import Http404,HttpResponseBadRequest, HttpResponseNotFound
from rest_framework import fields, serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from common.models import Institute, Language, studyField

from offers.serializers import SkillSerializer
from .models import  Education, Experience, Sector, companyType, profileModel,RecruiterProfile,AgencyProfile,authorizedViewers, userLanguage,userSkill
from .serializers import CompanySectorSerializer, CompanyTypeSerializer, EducationSerializer, ExperienceSerializer, ProfileSerializer, UserAddLanguageSerializer,appProfileSerializer,RecruiterSerializer,AgencySerializer,UserSkillSerializer, UserLanguageSerializer
from authapp.models import userAccount
from offers.models import Skill
from common.models import Position,Degree
from common.serializers import LanguageSerializer, PositionSerializer
@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def condidate_profile(request,pk):
    if request.method == 'GET':
        canView = authorizedViewers.objects.filter(user = pk,viewer_id = request.user.get_id()).exists()
        if canView:
            try:
                profile = profileModel.objects.get(user = pk)
            except:
                return JsonResponse({ "user":"not found"} , status= 404, safe=False)
            serializer = ProfileSerializer(profile)
            skills = userSkill.objects.filter(user = pk)
            skillsSerializer = UserSkillSerializer(skills,many=True)
            educations = Education.objects.filter(user = pk)
            educationSerializer = EducationSerializer(educations,many=True)
            return JsonResponse({ "info":serializer.data,"skills":skillsSerializer.data , "educations":educationSerializer.data}, safe=False)
        # else:
        #     return JsonResponse({"unauthorized ":"Action is not authorized for this user "},status = 401,safe=False)


@csrf_exempt
@api_view(['GET','POST',"PUT"])
@permission_classes([IsAuthenticated])
def candidateProfile(request):
    user = request.user.get_id()
    if str(request.user.get_user_type()) == "candidate":
        if request.method == 'GET':     
            try:
                profile = profileModel.objects.get(user = user)
            except Exception as e:
                # print(e)
                return JsonResponse({},status=404,safe=False)
            skills = userSkill.objects.filter(user = user)
            serializer = ProfileSerializer(profile)
            skillsSerialier = UserSkillSerializer(skills,many=True)
            educations = Education.objects.filter(user = request.user.get_id())
            educationSerializer = EducationSerializer(educations,many=True)
            
            experiences = Experience.objects.filter(user = request.user.get_id())
            experiencesSerializer = ExperienceSerializer(experiences,many=True)
            
            languages = userLanguage.objects.filter(user = request.user.get_id())
            langauagesSerializer = UserLanguageSerializer(languages,many=True)
            return JsonResponse({"userInfo":serializer.data,"skills":skillsSerialier.data,"educations":educationSerializer.data,"experiences":experiencesSerializer.data,"languages":langauagesSerializer.data},safe=False)
        elif request.method == 'POST':
            is_condidate = (str(userAccount.objects.get(id=request.user.get_id()).user_type) == "candidate") 
            if is_condidate:
                data={}
                
                # data["profile_pic"] = request.data["profile_pic"]
                # data["full_name"] = request.data["full_name"]
                # data["birthdate"] = request.data["birthdate"]
                # data["address"] = request.data["address"]
                # data["nationality"] = request.data["nationality"]
                # data["phone"] = request.data["phone"]
                # data["about"] = request.data["about"]
                # data["salary"] = request.data["salary"]
                # data["position"] = request.data["position"]
                # data["experience_years"] = request.data["experience_years"]
                # data["skills"] =  request.data["skills"]
                # for p in request.data: 
                #     data[p] = request.data[p]
                # data["skills"] = data["skills"].split(',')
                data= JSONParser().parse(request)
                # print(data)
                data["user"] = request.user.get_id()
                # print(data)
                # data["position"] = data["position"]["label"]
                data["position"]= Position.objects.get(label = data["position"])
                serializer = ProfileSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    for i in data['skills']:
                        skillsInfo = Skill.objects.get(label = i["label"])
                        skill = userSkill(user = request.user,label = skillsInfo )
                        skill.save()
                    # for i in data['languages']:
                    #     languageInfo = Language.objects.get(label = i["label"])
                    #     language = userLanguage(user = request.user,label = languageInfo )
                    #     language.save()
                    for i in data['educations']:
                        #print(i)
                        if(not Degree.objects.filter(label = i["degree"]["label"]).exists()):
                            continue
                        user = request.user
                        educationDgree =  Degree.objects.get(label = i["degree"]["label"])
                        isOngoing= i["isOngoing"]
                        endDate = None
                        if(i["endDate"] is not None):
                            endDate = i["endDate"].split("T")[0]    
                        if(i["startDate"] is None):
                            continue                 
                        startDate = i["startDate"].split("T")[0] 
                        if(not Institute.objects.filter(label = i["institute"]).exists()):
                                    continue
                        institute = Institute.objects.get(label = i["institute"])
                        field = studyField.objects.get(label = i["field"]["label"])
                        
                        description=i["description"]
                        if(not studyField.objects.filter(label = i["field"]["label"]).exists()):
                                continue
                        field = studyField.objects.get(label = i["field"]["label"])
                        Education.objects.create(user = user,field=field,degree = educationDgree,institute = institute,startDate=startDate,isOngoing=isOngoing,endDate = endDate,description=description)

                    for i in data['experiences']:
                        title =  i["title"]
                        isOngoing= i["isOngoing"]
                        startDate = i["startDate"].split("T")[0]
                        title = Position.objects.get(label = i["title"])
                        if i["endDate"]==None:
                            endDate =None
                        else:
                            endDate =i["endDate"].split("T")[0] 
                        company = i["company"]
                        description=i["description"]
                        Experience.objects.create(user= request.user,title = title,company = company,startDate=startDate,isOngoing=isOngoing,endDate =endDate ,description=description)
                    return JsonResponse(serializer.data, status=201)
                return JsonResponse(serializer.errors, status=400)
            else:
                return JsonResponse({"unauthorized ":"Only condidates can perform this operation "},status = 401,safe=False)
    return HttpResponse(status = 404)


@csrf_exempt
@api_view(['GET','POST',"PUT","DELETE"])
@permission_classes([IsAuthenticated])
def companyProfile(request,pk=None):
    is_employer = (userAccount.objects.get(id=request.user.get_id()).get_user_type())
    if str(is_employer) == "employer":
        if(request.method == 'GET'):
            try:
                if(pk is not None):
                    if(RecruiterProfile.objects.filter(id=pk).exists()):
                        company_profile = RecruiterProfile.objects.get(user = pk)

                    else:
                        return JsonResponse({"msg":"no profile corsepend to this account"},status=404, safe=False)

                else:
                    if(RecruiterProfile.objects.filter(user = request.user.get_id()).exists()):
                        company_profile = RecruiterProfile.objects.get(user = request.user.get_id())
                    else:
                        return JsonResponse({"msg":"no profile corsepend to this account"},status=404, safe=False)
                serializer = RecruiterSerializer (company_profile)
                return JsonResponse(serializer.data, safe=False)
            except:
                return HttpResponseNotFound
        elif request.method == 'POST':
                data = JSONParser().parse(request)
                # print(data)
                data["user"] = request.user.get_id()
                serializer = RecruiterSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=201)
                return JsonResponse(serializer.errors, status=400)
        elif request.method == 'PUT':
                if(pk is not None):
                    return JsonResponse({"msg":"you can't perform such action"},status=404, safe=False)
                data = JSONParser().parse(request)
                data["user"] = request.user.get_id()
                try:
                    company_profile = RecruiterProfile.objects.get(user = request.user.get_id())
                except:
                    return Http404
                serializer = RecruiterSerializer(company_profile,data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=201)
                return JsonResponse(serializer.errors, status=400)
        elif request.method == 'DELETE':
            if(pk is not None):
                return JsonResponse({"msg":"you can't perform such action"},status=404, safe=False)
            try:
                company_profile = RecruiterProfile.objects.get(user = request.user.get_id())
            except:
                return Http404
            company_profile.delete()
            return JsonResponse({"msg":"deleted"}, status=201)
    else:
        return JsonResponse({"unauthorized ":"Only condidates can perform this operation "},status = 401,safe=False)     


@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAgencyProfile(request,pk):
    if(request.method == 'GET'):
        agency_profile = AgencyProfile.objects.get(user = pk)
        serializer = AgencySerializer (agency_profile)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
@api_view(['GET',"PUT","DELETE","POST"])
@permission_classes([IsAuthenticated])
def userExperience(request,pk=None):
    if(str(request.user.user_type) =="candidate"):
        if(request.method == 'GET'):
            experiences = Experience.objects.filter(user=request.user.get_id())
            serializer = ExperienceSerializer (experiences,many=True)
            return JsonResponse(serializer.data, safe=False)
        if(request.method == 'POST'):
            data = JSONParser().parse(request)
            data["user"] = request.user.get_id()
            #print(data)
            if data["title"]:
                data["title"] = data["title"]["label"]
            if data["startDate"]:
                data["startDate"] = data["startDate"].split("T")[0]
            if data["endDate"]:
                data["endDate"] = data["endDate"].split("T")[0]
            
            serializer = ExperienceSerializer(data=data)
            #print(serializer.is_valid())
            if(serializer.is_valid()):
                
                serializer.save()
                return JsonResponse(serializer.data, safe=False)
            return JsonResponse(serializer.errors, safe=False)
        
        if(request.method == 'PUT'):
            if(pk == None):
                return JsonResponse(data={"msg: no id is passed"},safe= False)
            data = JSONParser().parse(request)
            data["user"] = request.user.get_id()
            if "title" in data and data["title"]:
                data["title"] = data["title"]["label"]
            if "endDate" in data and data["endDate"]:
                data["endDate"] = data["endDate"].split("T")[0]
            if "startDate" in data and data["endDate"]:
                data["endDate"] = data["endDate"].split("T")[0]
            exp = Experience.objects.get(id=pk) 
            if(exp.user.get_id() == int(request.user.get_id())):
                serializer = ExperienceSerializer(exp,data=data)
                if(serializer.is_valid()):
                    serializer.save()
                    return JsonResponse(serializer.data,safe = False, status = 200)       
                return JsonResponse(serializer.errors, safe=False , status=401 )
            return JsonResponse({"msg": "error has happend"}, safe=False)
                
        if(request.method == 'DELETE'):
            if(pk == None):
                return JsonResponse({"msg":"no id is passed"},safe= False)
            exp = Experience.objects.get(id=pk)
            if(exp.user.get_id() == request.user.get_id()):
                exp.delete()
                return JsonResponse(data={"msg":"deleted"},status=200)
            return JsonResponse({"msg":"error has happend"}, safe=False, status = 400)
    
@csrf_exempt
@api_view(['GET',"PUT","DELETE","POST"])
@permission_classes([IsAuthenticated])
def userEducation(request,pk=None):
    if(str(request.user.user_type) =="candidate"):
        if(request.method == 'GET'):
            experiences = Education.objects.filter(user=request.user.get_id())
            serializer = EducationSerializer (experiences,many=True)
            return JsonResponse(serializer.data, safe=False)
        if(request.method == 'POST'):
            data = JSONParser().parse(request)
            
            data["user"] = request.user.get_id()
            if data["startDate"]:
                data["startDate"] = data["startDate"].split("T")[0]
            if "endDate" in data and data["endDate"]:
                data["endDate"] = data["endDate"].split("T")[0]
            else :
                data["endDate"] = None
                
            if "degree" in data and data["degree"]:
                    data["degree"] = data["degree"]["label"]
            
            if "institute" in data and data["institute"]:
                data["institute"] = data["institute"]["label"]

            if "field" in data and data["field"]:
                    data["field"] = data["field"]["label"]
            #print(data)
            serializer = EducationSerializer(data=data)
            #print(serializer.is_valid())
            if(serializer.is_valid()):
                serializer.save()
                return JsonResponse(serializer.data, safe=False)
            return JsonResponse(serializer.errors, safe=False)
        
        if(request.method == 'PUT'):
            if(pk == None):
                return JsonResponse(data={"msg: no id is passed"},safe= False)
            data = JSONParser().parse(request)
            data["user"] = request.user.get_id()
            if data["startDate"]:
                data["startDate"] = data["startDate"].split("T")[0]
            if "endDate" in data and data["endDate"]:
                data["endDate"] = data["endDate"].split("T")[0]
            else :
                data["endDate"] = None
                
            if "degree" in data and data["degree"]:
                    data["degree"] = data["degree"]["label"]
            
            if "institute" in data and data["institute"]:
                data["institute"] = data["institute"]["label"]

            if "field" in data and data["field"]:
                    data["field"] = data["field"]["label"]
            exp = Education.objects.get(id=pk)
            if(exp.user.get_id() == int(request.user.get_id())):
                serializer = EducationSerializer(exp,data=data)
                if(serializer.is_valid()):
                    serializer.save()
                    return JsonResponse(serializer.data,safe = False, status = 200)       
                return JsonResponse(serializer.errors, safe=False , status=401 )
            return JsonResponse({"msg": "error has happend"}, safe=False)
                
        if(request.method == 'DELETE'):
            if(pk == None):
                return JsonResponse({"msg":"no id is passed"},safe= False)
            exp = Education.objects.get(id=pk)
            if(exp.user.get_id() == request.user.get_id()):
                exp.delete()
                return JsonResponse(data={"msg":"deleted"},status=200)
            return JsonResponse({"msg":"error has happend"}, safe=False, status = 400)
    return JsonResponse({"msg":"No Authority"}, safe=False, status = 400)


@csrf_exempt
@api_view(['GET',"PUT","DELETE","POST"])
@permission_classes([IsAuthenticated])
def userSkills(request,pk=None):
    
    if(str(request.user.user_type) =="candidate"):
        if(request.method == 'GET'):
            experiences = userSkill.objects.filter(user=request.user.get_id())
            serializer = UserSkillSerializer (experiences,many=True)
            return JsonResponse(serializer.data, safe=False)
        if(request.method == 'POST'):
            #delete previous skills 
            userSkill.objects.filter(user = request.user.get_id()).delete()
            data = JSONParser().parse(request)
            #print(data)
            for i in data["skills"]:                
                i["user"] = request.user.get_id()
            serializer = UserSkillSerializer(data=data["skills"],many=True)
            if(serializer.is_valid()):
                serializer.save()
                return JsonResponse(serializer.data, safe=False)
            return JsonResponse(serializer.errors, safe=False)
        
        if(request.method == 'PUT'):
            if(pk == None):
                return JsonResponse(data={"msg: no id is passed"},safe= False)
            data = JSONParser().parse(request)
            data["user"] = request.user.get_id()
            exp = UserSkillSerializer.objects.get(id=pk)
            if(exp.user.get_id() == int(request.user.get_id())):
                serializer = SkillSerializer(exp,data=data)
                if(serializer.is_valid()):
                    serializer.save()
                    return JsonResponse(serializer.data,safe = False, status = 200)       
                return JsonResponse(serializer.errors, safe=False , status=401 )
            return JsonResponse({"msg": "error has happend"}, safe=False)
                
        if(request.method == 'DELETE'):
            if(pk == None):
                return JsonResponse({"msg":"no id is passed"},safe= False)
            exp = UserSkillSerializer.objects.get(id=pk)
            if(exp.user.get_id() == request.user.get_id()):
                exp.delete()
                return JsonResponse(data={"msg":"deleted"},status=200)
            return JsonResponse({"msg":"error has happend"}, safe=False, status = 400)
    return JsonResponse({"msg":"No Authority"}, safe=False, status = 400)



@csrf_exempt
@api_view(['GET',"PUT","DELETE","POST"])
@permission_classes([IsAuthenticated])
def userLanguages(request,pk=None):
    
    if(str(request.user.user_type) =="candidate"):
        if(request.method == 'GET'):
            languages = userLanguage.objects.filter(user=request.user.get_id())
            serializer = UserLanguageSerializer(languages,many=True)
            return JsonResponse(serializer.data, safe=False)
        if(request.method == 'POST'):
            #delete previous skills 
            userLanguage.objects.filter(user = request.user.get_id()).delete()
            data = JSONParser().parse(request)
            #print(data)
            for i in data["languages"]:                
                i["user"] = request.user.get_id()
            #print(data["languages"])
            serializer = UserAddLanguageSerializer(data=data["languages"],many=True)
            if(serializer.is_valid()):
                serializer.save()
                return JsonResponse(serializer.data, safe=False)
            return JsonResponse(serializer.errors, safe=False)
                        
        if(request.method == 'DELETE'):
            if(pk == None):
                return JsonResponse({"msg":"no id is passed"},safe= False)
            exp = userLanguage.objects.get(id=pk,user = request.user.get_id())
            if(exp.user.get_id() == request.user.get_id()):
                exp.delete()
                return JsonResponse(data={"msg":"deleted"},status=200)
            return JsonResponse({"msg":"error has happend"}, safe=False, status = 400)
    return JsonResponse({"msg":"No Authority"}, safe=False, status = 400)



@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def comapnyTypeList(request):
    types = companyType.objects.all()
    serializer = CompanyTypeSerializer(types,many = True)
    return JsonResponse(serializer.data,status = 200 ,safe=False)



@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def comapnySectorsList(request):
    types = Sector.objects.all()
    serializer = CompanySectorSerializer(types,many = True)
    return JsonResponse(serializer.data,status = 200 ,safe=False)



@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def candidateList(request):
    if(str(request.user.user_type) == "employer"):
        query = request.query_params.dict()
        query['user__user_type'] = "candidate"
        if("skills" in query):
            query["skills"] = eval(query["skills"])
            profiles = [i.user for i in userSkill.objects.filter(label__in = query["skills"] )]
            profiles = profileModel.objects.filter(user__in=list(profiles))
            serializer = appProfileSerializer(profiles,many = True)
        return JsonResponse(serializer.data,status = 200 ,safe=False)
    else:
        return JsonResponse(status = 401 ,safe=False)
