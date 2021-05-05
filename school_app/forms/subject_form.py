from django.forms import ModelForm
from ..models import Subject

class SubjectForm(ModelForm):
    
    class Meta():
        model = Subject
        fields = '__all__' #['name', 'language']
        exclude = () # ['created_by', ]
