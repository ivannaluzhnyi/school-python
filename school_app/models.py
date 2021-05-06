from django.db import models
from django.contrib.auth.models import User
import os


from helpers import form_validator


def upload_path_handler(instance, filename):
    import os.path
    fn, ext = os.path.splitext(filename)
    return 'documents/classes%Y/%m/%d'
    # return "documents/classes/{id}{ext}".format(id=instance.pk, ext=ext)


class Subject(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=200)
    subject = models.ManyToManyField(Subject)
    user = models.ManyToManyField(User)
    year = models.IntegerField(validators=[form_validator.validate_year_class])
    doc = models.FileField(upload_to=upload_path_handler,
                           null=True, blank=True)

    def __str__(self):
        # print("------------------------------")

        return "%s (%s)" % (
            self.name,
            ", ".join(sb.name for sb in self.subject.all()),
        )


class Note(models.Model):
    note = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.note)
