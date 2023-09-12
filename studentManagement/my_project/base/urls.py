from django.urls import path
from . import views
from.views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('view_student/<str:pk>/', views.view_student, name='view_student'),
    path('delete_student/<str:pk>/', views.delete_student, name='delete_student'),
    path('all_students', views.all_students, name = 'all_students'),
    path('create_student', views.create_student, name = 'create_student'),
    path('update_student/<str:pk>/', views.update_student, name = 'update_student')
    
    
]
