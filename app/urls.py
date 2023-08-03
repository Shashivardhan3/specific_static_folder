from django.urls import path

from app.views import *


app_name='app'


urlpatterns=[
    path('specific_url_map/',specific_url_map,name='specific_url_map')
]