from django.db import models
from deliever.models import Deliever, Category
from django.contrib.auth.models import User

class Address(models.Model):
  name = models.CharField(max_length=50)
  price = models.IntegerField()

  class Meta:
    verbose_name_plural = "Addresses"

  def __str__(self) -> str:
    return self.name

class Item(models.Model):
  title = models.CharField(max_length=255)
  user = models.ForeignKey(User, on_delete=models.PROTECT)
  deliever = models.ForeignKey(Deliever, on_delete=models.PROTECT)
  image = models.ImageField(upload_to="item/")
  to_address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name="to_address")
  bulk = models.PositiveIntegerField()
  price = models.IntegerField()
  status = models.BooleanField(default=False)
  category = models.ForeignKey(Category, on_delete=models.PROTECT)

  def __str__(self) -> str:
    return self.title
  
class Comment(models.Model):
  name = models.CharField(max_length=100, null=True, blank=True)
  email = models.EmailField(null=True, blank=True)
  title = models.CharField(max_length=100, null=True, blank=True)
  text = models.TextField(null=True, blank=True)

  def __str__(self) -> str:
    return self.title