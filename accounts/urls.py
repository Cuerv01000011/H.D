from django.urls import path
from .views import login_view, admin_dashboard, user_dashboard

urlpatterns = [
    path('login/', login_view, name='login'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('user-dashboard/', user_dashboard, name='user_dashboard'),
]