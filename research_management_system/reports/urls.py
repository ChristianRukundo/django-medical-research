from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    path('', views.report_list, name='report_list'),
    path('detail/<int:id>/', views.report_detail, name='report_detail'),
]
