from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    # def __str__(self):
    #     return self

class Class(models.Model):
    name = models.CharField(max_length=200)
    subjects = models.ManyToManyField(Subject)
    user = models.ManyToManyField(User)
    year = models.IntegerField()

    def __str__(self):
        return self.name

class Note(models.Model):
    note = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.note)
