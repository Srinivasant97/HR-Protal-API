from django.db import models

# Create your models here.


class Applicant(models.Model):
    apl_id = models.AutoField(primary_key=True)
    apl_name = models.CharField(max_length=100)
    apl_email = models.EmailField(max_length=100)
    apl_phone = models.CharField(max_length=20)
    apl_joined = models.DateTimeField(auto_now_add=True)
    apl_linkedin = models.URLField(max_length=1000, null=True)

    class Meta:
        db_table = 'applicant'


class ApplicantDetails(models.Model):
    apl_details_id = models.AutoField(primary_key=True)
    apl_details_apl_id = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    apl_details_address = models.CharField(max_length=500)

    class Meta:
        db_table = 'applicant_details'


class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=100)
    emp_email = models.EmailField(max_length=100)
    emp_phone = models.CharField(max_length=20)
    emp_joined = models.DateTimeField(auto_now_add=True)
    emp_role = models.ForeignKey('Role', on_delete=models.CASCADE)

    class Meta:
        db_table = 'employee'


class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'role'


class EmployeePersonalDetails(models.Model):
    emp_personal_id = models.AutoField(primary_key=True)
    emp_personal_emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    emp_personal_address = models.CharField(max_length=500)
    emp_personal_education = models.CharField(max_length=500)

    class Meta:
        db_table = 'employee_personal_details'


class EmployeeAccountingDetails(models.Model):
    emp_accounting_id = models.AutoField(primary_key=True)
    emp_accounting_emp_id = models.ForeignKey(
        Employee, on_delete=models.CASCADE)
    emp_accounting_salary = models.IntegerField()
    emp_accounting_number = models.CharField(max_length=20)
    emp_accounting_pf = models.CharField(max_length=20)
    emp_accounting_uan = models.CharField(max_length=20)

    class Meta:
        db_table = 'employee_accounting_details'


class EmployeeJobDetails(models.Model):
    emp_job_id = models.AutoField(primary_key=True)
    emp_job_emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    emp_job_reporting_to = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='reporting_to')

    DEPARTMENT_CHOICES = (
        ('IT', 'IT'),
        ('HR', 'HR'),
        ('ACCOUNT', 'ACCOUNT'),
        ('SALES', 'SALES'),
        ('MARKETING', 'MARKETING'),
        ('FINANCE', 'FINANCE'),
        ('ADMIN', 'ADMIN'),
        ('OTHER', 'OTHER'),
    )

    DESIGNATION_CHOICES = (
        ('SDE1', 'SDE1'),
        ('SDE2', 'SDE2'),
        ('SDE3', 'SDE3'),
        ('SENIOR_SDE', 'SENIOR_SDE'),
        ('MANAGER', 'MANAGER'),
        ('DIRECTOR', 'DIRECTOR'),
        ('OTHER', 'OTHER'),
    )

    emp_job_department = models.CharField(
        max_length=100, choices=DEPARTMENT_CHOICES, default='IT')
    emp_job_designation = models.CharField(
        max_length=100, choices=DESIGNATION_CHOICES, default='SDE1')

    class Meta:
        db_table = 'employee_job_details'


class EmployeeAssetRegistry(models.Model):
    emp_asset_id = models.AutoField(primary_key=True)
    emp_asset_emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    emp_asset_name = models.CharField(max_length=100)
    emp_asset_description = models.CharField(max_length=500)

    class Meta:
        db_table = 'employee_asset_registry'


class JobApplication(models.Model):
    job_app_id = models.AutoField(primary_key=True)
    job_app_title = models.CharField(max_length=100)
    job_app_description = models.CharField(max_length=500)
    job_app_location = models.CharField(max_length=100)
    job_app_salary = models.IntegerField()
    job_app_hr_emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    job_app_manager_emp_id = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='manager_id')
    job_app_created = models.DateTimeField(auto_now_add=True)
    JON_APPLICATION_TYPES = (
        ('ENGINEERING', 'ENGINEERING'),
        ('ACCOUNTS', 'ACCOUNTS'),
        ('BUSINESS-AFFAIRS', 'BUSINESS-AFFAIRS'),
        ('SALES', 'SALES'),
        ('MARKETING', 'MARKETING'),
        ("DESIGN", "DESIGN"),
        ("OTHER", "OTHER"),
    )
    job_app_type = models.CharField(
        max_length=100, choices=JON_APPLICATION_TYPES, default='ENGINEERING')

    class Meta:
        db_table = 'job_application'


class JobApplicant(models.Model):
    job_appl_id = models.AutoField(primary_key=True)
    job_appl_apl_id = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    job_appl_app_id = models.ForeignKey(
        JobApplication, on_delete=models.CASCADE)
    APPLICATION_STATUS_CHOICES = (
        ('APPLIED', 'APPLIED'),
        ('PENDING', 'PENDING'),
        ('APPROVED', 'APPROVED'),
        ('SCHEDULED', 'SCHEDULED'),
        ('INTERVIEWED', 'INTERVIEWED'),
        ('SELECTED', 'SELECTED'),
        ('ACCEPTED', 'ACCEPTED'),
        ('REJECTED', 'REJECTED'),
    )
    job_appl_status = models.CharField(
        max_length=100, choices=APPLICATION_STATUS_CHOICES, default='APPLIED')
    job_apl_scheduled_time = models.DateTimeField(null=True)
    job_appl_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'job_applicant'
