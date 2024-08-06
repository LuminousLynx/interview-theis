from django.urls import path
from forklift import views

app_name = 'forklift'
urlpatterns = [
    path('', views.overview, name='overview'),
    path('status/', views.can_operate, name='can_operate'),
    path('Permission/', views.allow_operator, name='allow_operator'),
]