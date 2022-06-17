from django.urls import path
from .views import *
urlpatterns = [
    path("skills/",SkillsList),
    path("contract-types/",ContractTypesList),
    path("positions/",PostionsList),
    path("sectors/",SectorsList),
    path("offer-types/",OfferTypesList),
    path("degrees/",DegreesList),
    path("institutes/",InstitutesList),
    path("company-types/",CompanyTypesList),
    path("languages/",LanguagesList),
    path("sites/",SitesList),
    path("study-fields/",StudyFieldsList),
    

]
