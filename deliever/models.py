from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=50)

  class Meta:
    verbose_name = "Category"
    verbose_name_plural = "Categories"

  def __str__(self) -> str:
    return self.name

class Deliever(models.Model):
  name = models.CharField(max_length=100)
  profile_image = models.ImageField(upload_to="profile/", default="profile/user.png")
  work_time = models.CharField(max_length=50)
  activity = models.BooleanField(default=True)
  category = models.ForeignKey(Category, on_delete=models.PROTECT)

  def __str__(self) -> str:
    return self.name
