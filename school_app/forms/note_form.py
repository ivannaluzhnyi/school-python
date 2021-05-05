from django.forms import ModelForm
from ..models import Note


class NoteForm(ModelForm):

    class Meta():
        model = Note
        fields = '__all__'  # ['name', 'language']
        exclude = ()  # ['created_by', ]
