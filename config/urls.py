"""
URL configuration for config project.
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

# Custom error handler
handler403 = 'core.views.access_denied_view'

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),
    
    # Include ALL URLs from core/urls.py (including the root '' path)
    # The order matters: include core.urls FIRST so it catches the root URL
    path('', include('core.urls')),
    
    # Authentication URLs (these will be at /accounts/login/ etc.)
    path('accounts/login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]