from django.urls import path
from .views import *

urlpatterns = [
     
    path("", image2text, name="image2text"),
      
]