"""
URL configuration for config project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),
    
    # All core app URLs (this handles /, /water/, /fundi/, etc.)
    path('', include('core.urls')),
]