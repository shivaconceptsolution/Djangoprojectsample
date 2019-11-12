from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	return render(request,"scsapp/index.html")
def swaplogic(request):	
	a= request.GET['txt1']
	b= request.GET['txt2']
	temp=a
	a=b
	b=temp
	return HttpResponse("After swap value is "+a+","+b)
