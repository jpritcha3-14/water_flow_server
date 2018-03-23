from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('minute/', views.minute, name='minute'),
    path('hour/', views.hour, name='hour'),
    path('day/', views.day, name='day'),
    path('week/', views.week, name='week'),
    path('test/', views.test, name='test'),
]
