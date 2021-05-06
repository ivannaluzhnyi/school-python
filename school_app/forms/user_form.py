from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'  # ['name', 'language']
        exclude = ()  # ['created_by', ]
