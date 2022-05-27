from django.contrib import admin

# Register your models here.

from .models import Applicant, ApplicantDetails

admin.site.register(Applicant)
admin.site.register(ApplicantDetails)
