from django import forms
from .models import Staffs,Students
class StaffForm(forms.ModelForm):
    class Meta:
        model=Staffs
        fields='__all__'
class StudentForm(forms.ModelForm):
    class Meta:
        model=Students
        fields='__all__'


