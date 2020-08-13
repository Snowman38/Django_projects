from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name='Home'),
    path('contact/', views.Contact, name='Contact'),
    path('about/', views.About, name='About'),
    path('project/', views.Project_page, name='Project'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('project/<slug:slug>/', views.project_detail, name='project_detail')
]
