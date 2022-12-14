from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('order/', views.order, name='order'),
    path("", include("django.contrib.auth.urls")),
]
