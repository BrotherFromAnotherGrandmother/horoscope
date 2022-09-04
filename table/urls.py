from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_info_about_beautiful_table),
]