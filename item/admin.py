from django.contrib import admin
from .models import Address, Item, Comment

@admin.register(Address)
class AddressModelAdmin(admin.ModelAdmin):
  list_display = ("id", "name", "price")
  ordering = ('id',)

@admin.register(Item)
class ItemModelAdmin(admin.ModelAdmin):
  list_display = ("id", "title", "bulk", "price", "category", "status")
  ordering = ('id',)

@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
  list_display = ("id", "title", "text")
  ordering = ('id',)