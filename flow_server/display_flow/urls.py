from django.urls import path

from . import views

urlpatterns = [
    path('', views.current, name='current'),
    path('minute/', views.minute, name='minute'),
    path('minute_image/', views.minute_image, name='minute_image'),
    path('hour/', views.hour, name='hour'),
    path('hour_image/', views.hour_image, name='hour_image'),
    path('day/', views.day, name='day'),
    path('day_image/', views.day_image, name='day_image'),
    path('week/', views.week, name='week'),
    path('week_image/', views.week_image, name='week_image'),
    path('test/', views.test, name='test'),
]
