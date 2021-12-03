from django.db import models
from django.db.models.fields import CharField, FloatField


# Create your models here.
sex = (
        
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

maritalstatus = (
        
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Other', 'Other'),
    )

state = (
        
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jammu and Kashmir', 'Jammu and Kashmir'),
        ('Jharkhand', 'Jharkhand'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Tripura', 'Tripura'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttarakhand', 'Uttarakhand'),
        ('West Bengal', 'West Bengal'),
    )
class PatientEnrollmentForm(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age=models.IntegerField()
    sex=models.CharField(max_length=5,choices=sex)
    weight=CharField(max_length=10)
    hight=CharField(max_length=15)
    contactNumber=models.CharField(max_length=12)
    email=models.EmailField()
    city=CharField(max_length=20)
    state=CharField(max_length=20,choices=state)
    maritalStatus=CharField(max_length=10,choices=maritalstatus)
    parentsName=CharField(max_length=30)
    relationship=CharField(max_length=30)
    
