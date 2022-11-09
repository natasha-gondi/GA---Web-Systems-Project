from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('governors/', views.governors, name='governors'),
    path('national/', views.national, name="national"),
]

