from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.views import View

from .forms import PatienEnrollment
from .models import PatientEnrollmentForm


# Create your views here.

# this fuction for homepage
def home(request):
    return render(request,'crud/index.html')

# this fuction for show patient data from database
def showdata(request):
    data = PatientEnrollmentForm.objects.all()
    
    return render(request,'crud/appointmentData.html',{'data':data})

# this is class base views for patient registration
# 
class fillform(View):
    form = PatienEnrollment()
    def get(self,request):
        form = PatienEnrollment()
        return render(request,'crud/appointment.html',{'form':form})

    def post(self,request):
        if request.method == "POST" :
            fm = PatienEnrollment(request.POST)
            if fm.is_valid():
                first_name = fm.cleaned_data['first_name']
                last_name = fm.cleaned_data['last_name']
                age = fm.cleaned_data['age']
                sex = fm.cleaned_data['sex']
                weight = fm.cleaned_data['weight']
                hight = fm.cleaned_data['hight']
                contactNumber = fm.cleaned_data['contactNumber']
                email = fm.cleaned_data['email']
                city = fm.cleaned_data['city']
                state = fm.cleaned_data['state']
                maritalStatus = fm.cleaned_data['maritalStatus']
                parentsName = fm.cleaned_data['parentsName']
                relationship = fm.cleaned_data['relationship']
            
                reg = PatientEnrollmentForm(first_name=first_name, last_name=last_name, age=age,sex=sex,weight=weight,hight=hight,contactNumber=contactNumber,email=email,city=city,state=state,maritalStatus=maritalStatus,parentsName=parentsName,relationship=relationship)
                reg.save()
                
                return redirect('showdata')
            else:
                return HttpResponse(fm.errors.values())


            
    
    
            
            
            
        
    
            
            
            
            
      
            
            

    

# this fuction for delete data 
def delete_data(request,id):
    if request.method=='POST':
        pi=PatientEnrollmentForm.objects.get(pk=id)
        pi.delete()
        # messages.success(request,'Data deleted succesfully!!! ')
        return redirect(showdata)

 # this fuction for update registration form data
 
def update(request,id):
    if request.method=='POST':
        pi=PatientEnrollmentForm.objects.get(pk=id)
        fm = PatienEnrollment(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            
            # messages.success(request,'Data Updated Succesfully!!! ')
            return redirect(showdata)
    else:
        pi=PatientEnrollmentForm.objects.get(pk=id)
        fm = PatienEnrollment(instance=pi)

    return render(request,'crud/updatedata.html',{'form':fm})
        

        

    
