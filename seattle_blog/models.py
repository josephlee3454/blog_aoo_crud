from django.db import models
from django.urls import reverse
# title field
# author field
# body field
# Create your models here.
class SeattleBlog(models.Model):
  title = models.CharField(max_length=64)
  author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
  body =  models.TextField(max_length=364)

  def __str__(self):
    return self.title

  def get_abs_url(self):
    return reverse("SeattleBlog")

  
  def post_absolute_url(self):
    return reverse('home')
