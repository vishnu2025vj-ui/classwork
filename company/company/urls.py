from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from employees import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/employees/')),  
    path('employees/', views.employee_list, name='employee_list'),
]
