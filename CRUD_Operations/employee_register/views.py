from django.shortcuts import render
from .forms import EmployeeForm

# Create your views here.

def employe_list(request):
    return render(request, 'employee_register/employee_list.html'),

def employe_form(request):
    form = EmployeeForm()
    return render(request, 'employee_register/employee_form.html', {'form': form})

def employe_delete(request):
    pass