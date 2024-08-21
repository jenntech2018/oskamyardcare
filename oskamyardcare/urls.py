from django.urls import path
from services import views

urlpatterns = [
    path('', views.home, name='home'),
    path('success/', views.contactSubmitted, name='contactSubmitted'),
    path('privacy/', views.privacyPolicy, name='privacyPolicy'),
]