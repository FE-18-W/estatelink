from django.contrib import admin
from django.urls import path, include  # <-- The 'include' function MUST be imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # <-- This line MUST be present
]
