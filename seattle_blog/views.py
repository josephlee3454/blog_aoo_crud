from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import SeattleBlog
# from .models import SeattleWord
# Create your views here.
# title field
# author field
# body field
class HomePageView(TemplateView):
  template_name = 'home.html'
  model = SeattleBlog

class TreeListView(ListView):
  template_name = 'list.html'
  model = SeattleBlog

class CreatePageView(CreateView):
  template_name = 'create.html'
  model = SeattleBlog
  fields =  ['title', 'author', 'body']
  # success_url = reverse_lazy('Make_SeattleBloge')
  # fields =  ['__all__']

class PostDetailView(DetailView):
  template_name = 'detail.html'
  model = SeattleBlog

class UpdatePageView(UpdateView):
  template_name = 'update.html'
  model = SeattleBlog
  fields = ['title', 'body']

class DeleteView(DeleteView):
  template_name = 'delete.html'
  model = SeattleBlog
