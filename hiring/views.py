from .models import Applicant, ApplicantDetails, Employee, Role, EmployeePersonalDetails, EmployeeAccountingDetails, EmployeeJobDetails, EmployeeAssetRegistry, JobApplication, JobApplicant, Role
from rest_framework import serializers
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ApplicantSerializer, ApplicantDetailsSerializer, EmployeeSerializer, RoleSerializer, EmployeePersonalDetailsSerializer, EmployeeAccountingDetailsSerializer, EmployeeJobDetailsSerializer, EmployeeAssetRegistrySerializer, JobApplicantSerializer, JobApplicationSerializer


@api_view(['POST', 'GET'])
def applicant(request):
    if request.method == 'POST':
        serializer = ApplicantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def applicant_details(request):
    if request.method == 'POST':
        serializer = ApplicantDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def applicant_list(request, pk):
    if request.method == 'GET':
        if pk and pk > 0:
            applicants = Applicant.objects.filter(apl_id=pk)
        else:
            applicants = Applicant.objects.all()
        all_applicants = []
        for applicant in applicants:
            each_applicant = {
                ** ApplicantSerializer(applicant).data,
                **ApplicantDetailsSerializer(ApplicantDetails.objects.filter(
                    apl_details_apl_id=applicant.apl_id)[0]).data
            }
            all_applicants.append(each_applicant)
        return Response(all_applicants, status=status.HTTP_200_OK)


@api_view(['POST'])
def employee(request):
    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def role(request):
    if request.method == 'GET':
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def employee_personal_details(request):
    if request.method == 'POST':
        serializer = EmployeePersonalDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def employee_accounting_details(request):
    if request.method == 'POST':
        serializer = EmployeeAccountingDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def employee_job_details(request):
    if request.method == 'POST':
        serializer = EmployeeJobDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def employee_list(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        all_employees = []
        for employee in employees:
            each_employee = {
                ** EmployeeSerializer(employee).data,
            }
            employee_personal_data = EmployeePersonalDetails.objects.filter(
                emp_personal_emp_id=employee.emp_id)
            if len(employee_personal_data) > 0:
                employee_personal_details = EmployeePersonalDetailsSerializer(
                    employee_personal_data[0]).data
            else:
                employee_personal_details = {}
            each_employee = {
                **each_employee,
                **employee_personal_details
            }
            employee_accounting_data = EmployeeAccountingDetails.objects.filter(
                emp_accounting_emp_id=employee.emp_id)
            if len(employee_accounting_data) > 0:
                employee_accounting_details = EmployeeAccountingDetailsSerializer(
                    employee_accounting_data[0]).data
            else:
                employee_accounting_details = {}
            each_employee = {
                **each_employee,
                **employee_accounting_details
            }
            employee_job_data = EmployeeJobDetails.objects.filter(
                emp_job_emp_id=employee.emp_id)
            if len(employee_job_data) > 0:
                employee_job_details = EmployeeJobDetailsSerializer(
                    employee_job_data[0]).data
            else:
                employee_job_details = {}
            each_employee = {
                **each_employee,
                **employee_job_details
            }
            all_employees.append(each_employee)
        return Response(all_employees, status=status.HTTP_200_OK)


@api_view(['POST'])
def employee_asset_registry(request):
    if request.method == 'POST':
        serializer = EmployeeAssetRegistrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def job_application(request):
    if request.method == 'POST':
        serializer = JobApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def job_application_list(request):
    if request.method == 'GET':
        job_applications = JobApplication.objects.all()
        all_job_applications = []
        for job_application in job_applications:
            each_job_application = {
                ** JobApplicationSerializer(job_application).data,
                'hr': EmployeeSerializer(job_application.job_app_hr_emp_id).data,
                'manager': EmployeeSerializer(
                    job_application.job_app_manager_emp_id).data,
            }
            all_job_applications.append(each_job_application)
        return Response(all_job_applications, status=status.HTTP_200_OK)


@api_view(['POST'])
def job_applicant(request):
    if request.method == 'POST':
        serializer = JobApplicantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def job_applicant_list(request):
    if request.method == 'GET':
        job_applicants = JobApplicant.objects.all()
        all_job_applicants = []
        for job_applicant in job_applicants:
            each_job_applicant = {
                ** JobApplicantSerializer(job_applicant).data,
                'job_application': JobApplicationSerializer(
                    job_applicant.job_appl_app_id).data,
                'applicant': ApplicantSerializer(
                    job_applicant.job_appl_apl_id).data,
            }
            all_job_applicants.append(each_job_applicant)
        return Response(all_job_applicants, status=status.HTTP_200_OK)


@api_view(['PATCH'])
def job_applicant_update(request, pk):
    if request.method == 'PATCH':
        job_applicant = JobApplicant.objects.get(job_appl_id=pk)
        serializer = JobApplicantSerializer(job_applicant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def employee_by_email(request, email):
    if request.method == 'GET':
        # employee = Employee.objects.get(emp_email=email)
        # employee = {
        #     **EmployeeSerializer(employee).data,
        #     **RoleSerializer(employee.emp_role).data,
        # }

        try:
            employee = Employee.objects.get(emp_email=email)
            employee = {
                **EmployeeSerializer(employee).data,
                **RoleSerializer(employee.emp_role).data,
            }
            return Response(employee, status=status.HTTP_200_OK)
        except:
            try:
                applicant = Applicant.objects.get(apl_email=email)
                applicant = {
                    **ApplicantSerializer(applicant).data,
                    'role_name': 'APPLICANT'
                }
                return Response(applicant, status=status.HTTP_200_OK)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
