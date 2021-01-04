from django.urls import path

from . import views
urlpatterns = [
    # login / reg page
    path('', views.index),
]