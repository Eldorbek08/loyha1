from django.urls import path
from .views import malumot  

urlpatterns = [
    path('', malumot, name='loyha'),  
]
