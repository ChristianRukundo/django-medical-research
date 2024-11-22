from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('research_data.urls')),
    path('reports/', include('reports.urls')),
    path('users/', include('users.urls')),
    path('analytics/', include('analytics.urls')),
]
