from django.urls import path

from .views import *

app_name = 'workerstree'

urlpatterns = [
    
    path('workers/', position_list, name='position_list'),
    path('workers/add_workers/', add_workers, name='add_workers'),
    path('workers/<int:pk>/', get_position, name='get_position'),
    path('workers/<str:position>/', get_worker_by_position, name='get_position_worker'),
    
]