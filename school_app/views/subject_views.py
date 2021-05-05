from django.shortcuts import (get_object_or_404,
                              render,
                              redirect)
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from ..models import Subject as SubjectModel


def get(request, id):
    subject = get_object_or_404(SubjectModel, id=id)
    return HttpResponse(subject)


def get_all(request):
    subjects = SubjectModel.objects.all()
    return HttpResponse(subjects)


@csrf_exempt
def create(request):
    data = request.POST.dict()
    new_subject = SubjectModel.objects.create(**data)
    id = new_subject.id
    return redirect('subject_get', id)


@csrf_exempt
def update(request, id):
    data = request.POST.dict()
    SubjectModel.objects.filter(pk=id).update(**data)
    return redirect('subject_get', id)


@csrf_exempt
def delete(request, id):
    SubjectModel.objects.filter(pk=id).delete()
    return redirect('subject_get_all')
