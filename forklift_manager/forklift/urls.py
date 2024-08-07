from django.urls import path
from forklift import views

app_name = 'forklift'
urlpatterns = [
    path('', views.overview, name='overview'),
    path('status/', views.can_operate, name='can_operate'),
    path('operators/', views.toggle_operator, name='toggle_operator'),
    path('hours/', views.update_hours_run, name='hours_run'),
]