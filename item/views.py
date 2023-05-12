from django.shortcuts import render, redirect
from .forms import SignUpForm

def home(request):
  return render(request, "item/index.html")

def about(request):
  return render(request, "item/about.html")

def contact(request):
  return render(request, "item/contact.html")

def sign_up(request):
  if request.method == "POST":
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('item:login')
  else:
    form = SignUpForm()
  return render(request, 'item/sign_up.html', {'form': form})