from django.shortcuts import render, HttpResponse

def index(request):
    # return HttpResponse("This is home")
    return render(request, 'home.html')

def success(request):
    return render(request, 'success.html')