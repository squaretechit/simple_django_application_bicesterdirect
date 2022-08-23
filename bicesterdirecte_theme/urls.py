from django.urls import path
from .views import BicesterdirectTheme as theme

urlpatterns = [
    path('', theme.home, name='home'),
    path('privacy-policy/', theme.privacy_policy ,name='privacy-policy'),
    path('contact/', theme.contact, name='contact'),
]
