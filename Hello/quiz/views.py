from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def quiz(request):
    return render(request, 'quiz.html')
