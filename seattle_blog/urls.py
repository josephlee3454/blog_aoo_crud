from django.shortcuts import render
from django.urls import path
from .views import HomePageView, CreatePageView, PostDetailView, UpdatePageView, DeleteView
from django.urls import reverse_lazy

urlpatterns = [
  path('', HomePageView.as_view(), name='home'),
  path('post_detail/<int:pk>', PostDetailView.as_view(), name='detail'),
  path('post/new', CreatePageView.as_view(), name='create'),
  path('post/<int:pk>/edit/', UpdatePageView.as_view(), name='update'),
  path('post/<int:pk>/delete/', DeleteView.as_view(), name='delete'),

]