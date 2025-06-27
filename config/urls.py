from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loyha.urls')),
    path('', include('group.urls')),
    path('', include('news.urls')),
]
