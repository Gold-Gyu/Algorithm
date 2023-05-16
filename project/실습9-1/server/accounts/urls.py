from django.urls import path
from . import views

urlpatterns = [
  path("userinfo/", views.userinfo)
]