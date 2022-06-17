from django.urls import path 
from .views import applicationsList,applicationsItem

urlpatterns = [
    path('',applicationsList),
    path('<int:pk>/',applicationsItem),
]
