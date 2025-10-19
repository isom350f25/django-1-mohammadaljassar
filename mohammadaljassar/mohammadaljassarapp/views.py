from django.shortcuts import render
from django.http import HttpResponse


# Create your views here
name = "Mohammad Aljassar ID: 2251156364"
classes = ["Programming 2 ,Networking , Math 110"]
def myname_view(request):

    return HttpResponse(name)

def myclasses_view(request):

    return HttpResponse(classes)

def link_view(request):

    return render(request, "moh.html")