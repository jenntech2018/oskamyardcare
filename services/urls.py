from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('success/', views.contactSubmitted, name='contactSubmitted'),
    path('privacyPolicy/', views.privacyPolicy, name='privacyPolicy'),  # Changed here
]
