from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path("random", views.random),
    path('reset', views.reset)
]