from django.urls import path, include
from . import views
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('users/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('create/', views.create_research_project, name='create_research_project'),
    path('update/<int:pk>/', views.update_research_project, name='update_research_project'),
    path('delete/<int:pk>/', views.delete_research_project, name='delete_research_project'),
    path('projects/', views.view_research_projects, name='research_projects_list'),
]
