
from django.urls import path
from .views import offerCategoriesList, offersList,offerItem,getSkills
urlpatterns = [
    path('',offersList),
    path('<int:pk>/',offerItem),
    path('add-offer/',offersList),
    path('skills/',getSkills),
    path('categories/',offerCategoriesList)
    
]
    