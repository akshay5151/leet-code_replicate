from django.urls import path
from leetcodeadmin import views

urlpatterns = [
    path('admin', views.admin_create)
]
