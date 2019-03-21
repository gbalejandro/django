from django.urls import path, include

from generales.views import Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
]