from django.urls import path
from . import views

urlpatterns = [
    path('getAllReceipe/',views.getAllReceipe,name= 'getAllReceipe'),
    path('addReceipe/',views.addReceipe,name='addReceipe'),
]