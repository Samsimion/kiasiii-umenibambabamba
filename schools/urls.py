from django.urls import path
from . import views

urlpatterns = [
    path('register/primary/', views.register_primary_school, name = 'register_primary'),
    path('register/highschool/', views.register_high_school, name = 'register_highschool'),
    
]