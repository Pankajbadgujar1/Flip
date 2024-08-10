from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def index(request):
    
    #return HttpResponse("Blog home page......")
    return render(request,"blog/index.html")
