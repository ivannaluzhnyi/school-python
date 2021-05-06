from django.db import models
from django.contrib.auth.models import User


from helpers import form_validator


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

    def __str__(self):
        return self.name


class Note(models.Model):
    note = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.note)
