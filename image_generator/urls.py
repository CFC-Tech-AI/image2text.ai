from django.urls import path
from .views import *

urlpatterns = [
     
    path("", image2text, name="image2text"),

    path('image2text/', image2text_api, name='image2text_api'),
      
]