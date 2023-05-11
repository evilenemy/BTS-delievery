from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=50)

class Deliever(models.Model):
  name = models.CharField(max_length=100)
  profile_image = models.ImageField(upload_to="profile/")
  work_time = models.CharField(max_length=50)
  activity = models.BooleanField()
  category = models.ForeignKey(Category, on_delete=models.PROTECT)
