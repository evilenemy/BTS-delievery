from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import Comment, Address, Item
from deliever.models import Deliever, Category
import random

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

def random_choise_deliver(array):
  id = random.randint(1, len(array))
  return id

@login_required(login_url="/")
def create_order(request):
  try:
    categories = Category.objects.all()
    addresses = Address.objects.all()
    if request.method == "POST":
      category_ = request.POST.get("category")
      title = request.POST.get('title')
      bulk = request.POST.get('bulk')
      image = request.FILES.get('image')
      address_ = request.POST.get('address')
      address = Address.objects.get(id=address_)
      delivers = Deliever.objects.filter(category=category_)
      category = Category.objects.get(id=category_)
      if title == "" or address_ == "" or category_ == "" or bulk == "":
        return render(request, "item/create_order.html", {'categories': categories, "address": addresses, "delivers": delivers})
      if len(delivers) > 0:
        deliver = Deliever.objects.get(id=random_choise_deliver(delivers))
        item = Item.objects.create(title=title, image=image, to_address=address, bulk=bulk, category=category, status=False, user=request.user, deliever=deliver, price=address.price + (int(bulk) * 0.5))
        if item:
          return redirect("item:home")
      else:
        return render(request, "item/create_order.html", {"message": "Delivers not found!"})

    return render(request, "item/create_order.html", {'categories': categories, "addresses": addresses, "delivers": 0})
  except Exception as e:
    print(e)
    return render(request, "item/create_order.html", {"message": "An error occured!", 'categories': categories, "addresses": addresses})

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

def orders(request):
  orders = Item.objects.filter(user=request.user)
  return render(request, "item/orders.html", {"orders": orders})