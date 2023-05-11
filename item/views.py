from django.shortcuts import render

def home(request):
  return render(request, "item/index.html")

def about(request):
  return render(request, "item/about.html")

def contact(request):
  return render(request, "item/contact.html")
