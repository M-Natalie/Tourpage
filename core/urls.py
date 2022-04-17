from django.urls import path
from .views import profile, HomeView
from django.conf import settings


urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('profile/', profile, name='profile'),
]