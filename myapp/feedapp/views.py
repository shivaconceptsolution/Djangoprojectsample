from django.shortcuts import render

def index(request):
	return render(request,"feedapp/index.html")
def about(request):
	return render(request,"feedapp/about.html")	
def contact(request):
	return render(request,"feedapp/contact.html")	
def service(request):
	return render(request,"feedapp/service.html")			
