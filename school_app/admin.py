from django.contrib import admin
from .models import Class, Subject, Promotion, Note


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class NoteAdmin(admin.ModelAdmin):
    list_display = ('note', 'subject')

admin.site.register(Class)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Promotion)
admin.site.register(Note, NoteAdmin)

# Register your models here.
