# employee_management/urls.py
from django.contrib import admin
from django.urls import path
from employees import views  # Make sure this import exists

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.employee_list, name='employee_list'),  # Main list view
    path('books/', views.employee_list, name='book_list'),  # Add this alias
    path('new/', views.employee_create, name='employee_create'),
    path('<int:pk>/edit/', views.employee_update, name='employee_update'),
    path('<int:pk>/delete/', views.employee_delete, name='employee_delete'),
]