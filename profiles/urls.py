from django.urls import path, re_path
from .views import candidateList, comapnySectorsList, comapnyTypeList, candidateProfile,getAgencyProfile,companyProfile,condidate_profile, userEducation, userExperience, userLanguages, userSkills



urlpatterns = [
    path('candidate/',candidateProfile),
    path('candidate/<int:pk>/', condidate_profile),
    path('employer/',companyProfile),
    path('employer/<int:pk>/',companyProfile),
    path('agency/<int:pk>/',getAgencyProfile),
    path('experience/',userExperience),
    path('experience/<int:pk>/',userExperience),
    path('education/',userEducation),
    path('education/<int:pk>/',userEducation),
    path('skill/',userSkills),
    path('skill/<int:pk>/',userSkills),
    path('sector/',comapnySectorsList),
    # path('sector/<int:pk>/',userSkills),
    path('companyType/',comapnyTypeList),
    path('languages/',userLanguages),
    path('languages/<int:pk>/',userLanguages),
    path('candidates-list/',candidateList),
    # path('companyType/<int:pk>/',userSkills),
    
    
]
