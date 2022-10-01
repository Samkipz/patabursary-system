from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path("register", views.registerView, name="register"),
    path("login", views.loginView, name="login"),
    path("staff_dashboard", views.staff_dashboard, name="staff_dashboard"),
    path("approve/<int:id>", views.approve, name="approve"),
    path("applicant_dashboard", views.applicant_dashboard, name="applicant_dashboard"),
    path("applicant_profile/<int:id>", views.applicant_profile, name="applicant_profile"),
    path("update_profile", views.update_profile, name='update_profile'),
]