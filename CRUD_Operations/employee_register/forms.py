from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        # fields = ("fullname","mobile",)
        fields = "__all__"
