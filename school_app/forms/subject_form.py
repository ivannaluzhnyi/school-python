from django.forms import ModelForm
from ..models import Subject, User
from django import forms


class SubjectForm(ModelForm):
    # Student = forms.ModelMultipleChoiceField(queryset = User.objects.filter(
    # groups__name__in=['student']))
    # user =  forms.ModelMultipleChoiceField(queryset = User.objects.filter(
    #     groups__name__in=['professor']))
    class Meta():
        
        model = Subject
        fields = '__all__'  # ['name', 'language']  
        exclude = ()  # ['created_by', ]
    # def __init__(self, users=None, **kwargs):
    #     super(SubjectForm, self).__init__(**kwargs)
    #     self.fields['user'].queryset = User.objects.filter(
    # groups__name__in=['professor'])
