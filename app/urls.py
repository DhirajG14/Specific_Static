from django.urls import path
from app.views import *
app_name='app'

urlpatterns=[
    path('specific_static/',specific_static,name='specific_static')
]