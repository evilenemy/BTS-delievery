from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
  name = models.CharField(max_length=50)

  class Meta:
    verbose_name = "Category"
    verbose_name_plural = "Categories"

  def __str__(self) -> str:
    return self.name

class Deliever(models.Model):
  user = models.ForeignKey(User, on_delete=models.PROTECT)
  name = models.CharField(max_length=100)
  profile_image = models.ImageField(upload_to="profile/", default="profile/user.png", null=True, blank=True)
  work_time = models.CharField(max_length=50, null=True, default='no limit')
  activity = models.BooleanField(default=True)
  category = models.ForeignKey(Category, on_delete=models.PROTECT)

  def __str__(self) -> str:
    return self.name
