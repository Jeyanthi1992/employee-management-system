from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='login', permanent=False)),

    path('home/', views.home, name='home'),
    path("about/", views.about, name="about"),
    path("service/", views.service, name="service"),
    path("employee-form/", views.employee_form, name="employee_form"),
    path("employee-list/", views.employee_list, name="employee_list"),
    path("employees/edit/<int:id>/", views.employeeedit, name="employeeedit"),
    path("employees/delete/<int:id>/", views.employeedelete, name="employeedelete"),
    path("employee/<int:id>/", views.singleemployee, name="singleemployee"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
]