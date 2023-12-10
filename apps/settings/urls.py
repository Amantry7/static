from django.urls import path
from apps.settings.views import *

urlpatterns = [
    path('', index,name='index'),
    path('1', index2, name='index2'),
    path('2', index3, name='index3')
    
]