from django.urls import path
from siteapp.views import index

app_name='siteapp'
urlpatterns=[
    path('',index),
]