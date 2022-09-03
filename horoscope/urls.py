from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='horoscope_index'),
    path('type/', views.types_sign_zodiac, name='typeHoroscope'),
    path('type/<type_zodiac>', views.get_info_about_type_zodiac),
    path('<int:sign_zodiac>/', views.get_info_about_zodiac_sign_by_number),
    path('<str:sign_zodiac>/', views.get_info_about_zodiac_sign, name='horoscope_name'),
    path('/beautiful_table/', views.get_info_about_beautiful_table, name='beautiful_table'),
]