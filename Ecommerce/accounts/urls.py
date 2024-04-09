from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register_request, name="register_request"),
    path('terms/', views.terms, name="terms"),
    path('login/', views.login_request, name="login_request"),
    path('logout/', views.logout_request, name="logout"),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
]
