from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, "index.html")

def about(request):
    return HttpResponse("This is about Page")

def services(request):
    return HttpResponse("This is Services Page")

def contact(request):
    return HttpResponse("This is contact Page")