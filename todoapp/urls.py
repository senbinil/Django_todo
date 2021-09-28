from django import forms
from django.urls import path
from .views import Listme, add_task, delete, delete_me, details_view, empty, home, update_task, update_view
from django.conf.urls import static
from django.conf import settings
app_name='todo'
urlpatterns=[
    path('',home,name='home'),
    path('delete/<int:taskid>/',delete,name='delete'),
    path('edit/<int:taskid>/',update_task,name='edit'),
    path('list',Listme.as_view(),name='index'),
    path('more/<int:pk>/',details_view.as_view(),name='more'),
    path('update/<int:pk>/',update_view.as_view(),name='update'),
    path('create',add_task.as_view(),name='create'),
    path('remove/<int:pk>/',delete_me.as_view(),name='remove'),
    path('empty',empty,name='empty'),

]