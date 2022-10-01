from django.urls import path
from . import views

app_name = 'bursaryapp'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path("Addbursary/", views.Addbursary, name="Addbursary"),
    path("Addparameters/<int:id>'", views.Addparameters, name="Addparameters"),
    path("Editbursary/<int:id>'", views.Editbursary, name="Editbursary"),
    path("Generateapplicants/<int:id>'", views.Generateapplicants, name="Generateapplicants"),
    
    path("bursary/<int:id>'", views.bursary_details, name="bursary_details"),
    path("Applicants/'", views.Applicants, name="Applicants"),
    path("applyBursary/<int:id>'", views.applyBursary, name="applyBursary"),
    # path('bursary/<int:pk>', views.BursaryDetailView.as_view(), name='bursary_details'),
]