from .models import Applicant, ApplicantDetails, Employee, Role, EmployeePersonalDetails, EmployeeAccountingDetails, EmployeeJobDetails, EmployeeAssetRegistry, JobApplicant, JobApplication
from rest_framework import serializers


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = '__all__'

    def create(self, validated_data):
        applicant = Applicant.objects.create(**validated_data)
        return applicant


class ApplicantDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicantDetails
        fields = '__all__'

    def create(self, validated_data):
        applicant_details = ApplicantDetails.objects.create(**validated_data)
        return applicant_details


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        employee = Employee.objects.create(**validated_data)
        return employee


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

    def create(self, validated_data):
        role = Role.objects.create(**validated_data)
        return role


class EmployeePersonalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeePersonalDetails
        fields = '__all__'

    def create(self, validated_data):
        employee_personal_details = EmployeePersonalDetails.objects.create(
            **validated_data)
        return employee_personal_details


class EmployeeAccountingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeAccountingDetails
        fields = '__all__'

    def create(self, validated_data):
        employee_accounting_details = EmployeeAccountingDetails.objects.create(
            **validated_data)
        return employee_accounting_details


class EmployeeJobDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeJobDetails
        fields = '__all__'

    def create(self, validated_data):
        employee_job_details = EmployeeJobDetails.objects.create(
            **validated_data)
        return employee_job_details


class EmployeeAssetRegistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeAssetRegistry
        fields = '__all__'

    def create(self, validated_data):
        employee_asset_registry = EmployeeAssetRegistry.objects.create(
            **validated_data)
        return employee_asset_registry


class JobApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplicant
        fields = '__all__'

    def create(self, validated_data):
        job_applicant = JobApplicant.objects.create(**validated_data)
        return job_applicant


class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'

    def create(self, validated_data):
        job_application = JobApplication.objects.create(**validated_data)
        return job_application
