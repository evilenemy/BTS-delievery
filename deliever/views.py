from django.shortcuts import render

def login(request):
  return render(request, "deliever/login.html")

def home(request):
  return render(request, "deliever/home.html")