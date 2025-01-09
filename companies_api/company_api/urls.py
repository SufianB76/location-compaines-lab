from django.urls import path
from . import views

urlpatterns = [
    path('api/company', views.CompanyList.as_view(), name='company_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/company/<int:pk>', views.CompanytDetail.as_view(), name='company_detail'), # api/contacts will be routed to the ContactDetail view for handling
]