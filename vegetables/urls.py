from django.urls import path
from . import views

urlpatterns = [
    path('getAllReceipe/',views.getAllReceipe,name= 'getAllReceipe'),
    path('addReceipe/',views.addReceipe,name='addReceipe'),
    path('delete-receipe/<int:id>/',views.deleteReceipe,name='deleteReceipe'),
    path('updateReceipe/<int:id>/',views.updateReceipe,name='updateReceipe')
]