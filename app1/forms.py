from django import forms
from app1.models import UserRole
class UserRoleForm(forms.ModelForm):
     class Meta():
         model=UserRole
         fields='__all__'
