from django.shortcuts import render, redirect
from .models import Deliever
from item.models import Item

def orders(request):
  try:
    deliver = Deliever.objects.get(user=request.user)
    orders = Item.objects.filter(deliever=deliver).order_by('status')
    return render(request, "deliever/orders.html", {'orders': orders})
  except Exception as e:
    print(e)
    return redirect("item:home")

def view_profile(request, id):
  deliver = Deliever.objects.get(id=id)
  deliver.name = str(deliver.name).title()
  return render(request, 'deliever/view_profile.html', {'deliver': deliver})

def complete_order(request, id):
  order = Item.objects.get(id=id)
  deliver = Deliever.objects.get(id=order.deliever.id)
  order.status = True
  deliver.activity = True
  deliver.price += order.price
  deliver.save()
  order.save()
  return redirect("deliver:orders")