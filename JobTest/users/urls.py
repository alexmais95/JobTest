from django.urls import path

from .views import *

app_name = 'users'

urlpatterns = [
    
    path('login/', login_viev, name='login'),
    path('logout/', logout_viev, name='logout'),
    path('registration/', registration_viev, name='regist'),
]