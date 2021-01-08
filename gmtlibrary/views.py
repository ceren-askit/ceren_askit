from django.shortcuts import render
from gmtlibrary.models import *
from django.core.files.storage import FileSystemStorage

# Create your views here.
def home(request, *args, **kwargs):
    academician = Academician.objects.all()
    cname = Course.objects.all()
    context = {
        'academician': academician,
        'course': cname,

    }
    return render(request, 'gmtlibrary/home.html', context)

# def courses(request, *args, **kwargs ):

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'gmtlibrary/upload.html', context)