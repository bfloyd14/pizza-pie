from typing import Any
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Pizza

# Create your views here.

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')  

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cat-index')
    else:
      error_message = 'Invalid sign up - try again'

  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context) 

class PizzaList(LoginRequiredMixin, ListView):
  model = Pizza
  template_name = 'pizzas/index.html'

class PizzaCreate(LoginRequiredMixin, CreateView):
  model = Pizza
  fields = ['name', 'ingredients', 'description', 'location']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class PizzaDetail(LoginRequiredMixin, DetailView):
  model = Pizza

class PizzaUpdate(LoginRequiredMixin, UpdateView):
  model = Pizza
  fields = ['name', 'ingredients', 'description', 'location']

class PizzaDelete(LoginRequiredMixin, DeleteView):
  model = Pizza
  success_url = '/pizzas/'  

  
  
    