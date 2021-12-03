from django.contrib import admin
from .models import PatientEnrollmentForm
# Register your models here.
@admin.register(PatientEnrollmentForm)
class PatientEnrollmentFormAdmin(admin.ModelAdmin):
 list_display = ('id', 'first_name','last_name','age','sex','weight','hight','contactNumber' ,'email','city','state','maritalStatus','parentsName','relationship')
