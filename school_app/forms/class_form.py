from django.forms import ModelForm
from ..models import Class


class ClassForm(ModelForm):

    class Meta():
        model = Class
        fields = '__all__'  # ['name', 'language']
        exclude = ()  # ['created_by', ]
