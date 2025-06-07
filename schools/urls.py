from django.urls import path
from . import views

urlpatterns = [
    path('primary-schools/', views.primary_schools),
    path('high-schools/', views.high_schools),
]