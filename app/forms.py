from django import forms
from .models import employee

class employeeform(forms.ModelForm):
    class Meta:
        model=employee
        fields=('Name','Email','Age','Mobile_no')







    