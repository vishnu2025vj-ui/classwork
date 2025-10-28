from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('result/<str:student_name>/', views.view_result, name='view_result'),
]
