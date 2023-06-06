from django.contrib import admin
from .models import Category, Deliever

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
  list_display = ("id", "name")
  ordering = ('id',)

@admin.register(Deliever)
class DeliverModelAdmin(admin.ModelAdmin):
  list_display = ("id", "name", "category", "work_time", "price", "activity")
  ordering = ('id',)