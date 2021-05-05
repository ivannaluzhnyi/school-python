from django.contrib import admin
from .models import Class, Subject, Note
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class NoteAdmin(admin.ModelAdmin):
    list_display = ('note', 'subject', 'user')

@admin.display(description='nb_eleves')
def count_students(obj):
    print(obj.user.all())
    return ("%d" % len(obj.user.all()))

class ClassAdmin(admin.ModelAdmin):
    list_display = ("name", count_students)

admin.site.register(Class, ClassAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Note, NoteAdmin)

# Register your models here.
