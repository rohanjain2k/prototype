from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable1':"I am great.",
        'variable2':"You are great."
    }
    return render(request,'index.html', context)
    #return HttpResponse('This is Home Page')
def about(request):
    return render(request,'about.html')
    #return HttpResponse('This is About Page')
def services(request):
    return render(request,'services.html')
    #return HttpResponse('This is Services Page')
def contact(request):
    return render(request,'contact.html')
    #return HttpResponse('This is Contact Page')