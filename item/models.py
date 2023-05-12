from django.db import models
from deliever.models import Deliever, Category
from django.contrib.auth.models import User

class Address(models.Model):
  name = models.CharField(max_length=50)
  price = models.IntegerField()

  def __str__(self) -> str:
    return self.name

class Item(models.Model):
  title = models.CharField(max_length=255)
  user = models.ForeignKey(User, on_delete=models.PROTECT)
  deliever = models.ForeignKey(Deliever, on_delete=models.PROTECT)
  image = models.ImageField(upload_to="item/")
  from_address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name="from_address")
  to_address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name="to_address")
  bulk = models.PositiveIntegerField()
  price = models.IntegerField()
  status = models.BooleanField(default=False)
  category = models.ForeignKey(Category, on_delete=models.PROTECT)

  def __str__(self) -> str:
    return self.title