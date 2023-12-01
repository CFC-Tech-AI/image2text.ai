from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),    
    path("image2text/", image2text, name="image2text"),
      
]