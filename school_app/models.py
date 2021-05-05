from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    classes = models.ManyToManyField(Class)

class Class(models.Model):
    name = models.CharField(max_length=200)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)

class Promotion(models.Model):
    name = models.CharField(max_length=200)
    classes = models.OneToManyField(Class)

class Note(models.Model):
    note = models.IntegerField(max_length=11)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    

