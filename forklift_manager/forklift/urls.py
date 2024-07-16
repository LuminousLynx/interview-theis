from django.urls import path
from forklift import views

app_name = 'forklift'
urlpatterns = [
    path('', views.overview, name='overview'),
    
    path('Permission/', views.allow_operator, name='allow_operator'),
]