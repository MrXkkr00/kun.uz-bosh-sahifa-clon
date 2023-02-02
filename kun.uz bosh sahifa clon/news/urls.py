from django.urls import path
from .views import Homepageviews

urlpatterns = [
    path('',Homepageviews.as_view(),name='home')
]