from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('accounts/signup/', views.signup, name='signup'),
  path('about/', views.about, name='about'),
  path('pizzas/', views.PizzaList.as_view(), name='pizza-index'),
  path('pizzas/create/', views.PizzaCreate.as_view(), name='pizza-create'),
  path('pizzas/<int:pk>/', views.PizzaDetail.as_view(), name='pizza-detail'),
]
