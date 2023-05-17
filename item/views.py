from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import Comment, Address, Item
from deliever.models import Deliever, Category

def home(request):
  return render(request, "item/home.html")

def about(request):
  return render(request, "item/about.html")

def contact(request):
  if request.method == "POST":
    name = request.POST.get('name')
    email = request.POST.get('email')
    title = request.POST.get('title')
    text = request.POST.get('text')
    try:
      comment = Comment.objects.create(name=name, email=email, title=title, text=text)
      if comment:
        return render(request, "item/contact.html", {"message": "Your message has been sent. Thank you!"})
    except Exception as e:
      print(e)
  return render(request, "item/contact.html") 

@login_required(login_url="/")
def create_order(request):
  categories = Category.objects.all()
  addresses = Address.objects.all()
  if request.method == "POST":
    delivers = Deliever.objects.filter(category=request.POST.get("category"))
    title = request.POST.get('title')
    bulk = request.POST.get('bulk')
    image = request.FILES.get('image')
    if not title:
      return render(request, "item/create_order.html", {'categories': categories, "address": addresses, "delivers": delivers})

  return render(request, "item/create_order.html", {'categories': categories, "address": addresses, "delivers": 0})

def signup(request):
  if request.method == "POST":
    email = request.POST.get('email')
    username = request.POST.get('username')
    password = request.POST.get('password')
    confirmation = request.POST.get('confirmation')
    if password != confirmation:
      return render(request, 'item/login_signup.html', {'signup_message': "Passwords must match."})
    try:
      user = User.objects.create_user(username, email, password)
    except IntegrityError:
      return render(request, "item/login_signup.html", {"signup_message": "User is already taken."})
    login(request, user)
    return redirect("item:home")
  return redirect("item:login")
