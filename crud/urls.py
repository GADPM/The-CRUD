from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_crud.urls')),  # Inclui as URLs do app app_crud
]