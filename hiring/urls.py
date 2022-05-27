from django.urls import path
from .views import (
    applicant_list,
    applicant,
    applicant_details,
    employee,
    role,
    employee_personal_details,
    employee_accounting_details,
    employee_job_details, job_application, job_applicant, job_application_list, job_applicant_list
)
from . import views

urlpatterns = [
    path('applicant', views.applicant),
    path('applicant_list/<int:pk>', views.applicant_list),
    path('applicant_details', views.applicant_details),
    path('employee', views.employee),
    path('role', views.role),
    path('employee_personal_details', views.employee_personal_details),
    path('employee_accounting_details', views.employee_accounting_details),
    path('employee_job_details', views.employee_job_details),
    path('employee_list', views.employee_list),
    path('job_application', views.job_application),
    path('job_applicant', views.job_applicant),
    path('job_application_list', views.job_application_list),
    path('job_applicant_list', views.job_applicant_list),
]
