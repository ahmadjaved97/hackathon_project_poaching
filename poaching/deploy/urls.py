from django.urls import path
from . import views

urlpatterns = [
    path('alerts/', views.alerts, name='alerts'),
    path('map/', views.maps, name='camera'),
    path('map/<int:pk>/', views.maps, name='map_details')
]



