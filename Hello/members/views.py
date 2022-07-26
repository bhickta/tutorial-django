from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_user(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'authenticate/done.html')
        else:
            # return redirect ('home')
            messages.success(request, ('There was an error in username or password - kindly try again'))
            return render(request, 'authenticate/login.html')
    else:
        return render(request, 'authenticate/login.html')
