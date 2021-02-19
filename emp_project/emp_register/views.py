
from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.
# It can handle the each of crud requests.

def emp_list(request):              # It shows employee records list.
    context={'emp_list':Employee.objects.all()}
    return render(request,'emp_register/emp_list.html',context)

def emp_form(request, id=0):       # Inside this, we will deal with GET and POST request to insert and update operations.
    if request.method == 'GET':
        if id == 0:
            form = EmployeeForm()
        else:
            employee=Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, 'emp_register/emp_form.html', {'form':form})
    else :
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form=EmployeeForm(request.POST,instance=employee)
        
        if form.is_valid():
            form.save()
        return redirect('/employee/list')
    

def emp_delete(request,id):             # To delete the existing employee record.
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')