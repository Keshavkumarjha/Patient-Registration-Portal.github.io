from django.forms import ModelForm
from .models import PatientEnrollmentForm

class PatienEnrollment(ModelForm):
    class Meta:
        model = PatientEnrollmentForm
        fields = '__all__'
        