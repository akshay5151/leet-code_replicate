from django.urls import path
from problem import views

urlpatterns = [
    path('topic', views.create),
    path('topic/<str:topic_id>', views.get),
    path('difficulty', views.create_difflevel),
    path('difficulty/<str:diff_id>', views.get_difflevel),
    path('problem', views.createproblem),
    path('problem/<str:problem_id>', views.getproblem)
]
