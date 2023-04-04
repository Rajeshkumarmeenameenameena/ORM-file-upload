from django.shortcuts import render,HttpResponse
from .form import studentform
from .models import *
# Create your views here.
def home(request):
    form=studentform()
    context={
        'form':form
    }
    return render(request,'app/home.html',context)

def studentdata(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phoneno=request.POST['phoneno']
        print(name,email,phoneno)
        mydata=student(name=name,email=email,phoneno=phoneno)
        mydata.save()
    return HttpResponse('submit form')

def file(request):
    if request.method=='POST':
        a=request.FILES['file']
        data=savefile.objects.create(file=a)
        data.save()
        print(a)
    return HttpResponse('savefile')