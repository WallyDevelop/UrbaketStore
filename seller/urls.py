from django.urls import path
from . import views

urlpatterns = [
    path('', views.sellerdashboard, name="selldash")
]