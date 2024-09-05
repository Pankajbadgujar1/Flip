from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def index(request):
    #return HttpResponse("Shop home page......")
    return render(request,"shop/index.html")

def about(request):
    return HttpResponse("This is aboutUs Page")

def contact(request):
    return HttpResponse("This is contact Page")

def search(request):
    return HttpResponse("This is search Page")

def productView(request):
    return HttpResponse("This is productView Page")

def checkout(request):
    return HttpResponse("This is checkout Page")


