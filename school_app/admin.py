from django.contrib import admin
from .models import Class, Subject, Note
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class NoteAdmin(admin.ModelAdmin):
    list_display = ('note', 'subject', 'user')


admin.site.register(Class)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Note, NoteAdmin)

# Register your models here.
