
from django.shortcuts import render
from django.http import HttpResponse
from .image2text import image_to_text
from PIL import Image
from io import BytesIO
import io
import base64
from django.views.decorators.csrf import csrf_exempt
from django import forms


class ImageUploadForm(forms.Form):
    image = forms.ImageField()


@csrf_exempt
def image2text(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            output = image_to_text(image)
            return render(request, 'image2textresult.html', {'output': output})
    else:
        form = ImageUploadForm()
    return render(request, 'image2text.html', {'form': form})




        
        
        
