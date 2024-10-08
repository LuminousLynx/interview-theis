from django.urls import path
from forklift import views

app_name = 'forklift'
urlpatterns = [
    path('', views.overview, name='overview'),
    path('status/', views.can_operate, name='can_operate'),
    path('operators/', views.toggle_operator, name='toggle_operator'),
    path('hours/', views.update_hours_run, name='hours_run'),
    path('next_check/', views.update_next_check, name='next_check'),
    path("auto_check/", views.auto_check, name="auto_check"),                #see if needed
    path("repair/", views.request_repair, name="request_repair"),
    path("repair/end", views.end_repair, name="end_repair"),
]