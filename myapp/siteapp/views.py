from django.shortcuts import render

def index(request):
	return render(request,"siteapp/index.html")
def about(request):
	return render(request,"siteapp/about.html")
def contact(request):
	return render(request,"siteapp/contact.html")
def service(request):
	return render(request,"siteapp/service.html")			
