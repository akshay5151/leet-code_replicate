from django.urls import path
from company import views

urlpatterns = [
    path('company', views.create),
    path('company/<str:company_id>', views.get),
    path('companyproblems', views.create_comProblem),
    path('companyproblems/<str:_id>', views.get_comProblem),
]