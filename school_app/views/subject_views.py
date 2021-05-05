from django.shortcuts import (get_object_or_404,
                              render,
                              redirect)
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from ..models import Subject as SubjectModel
from django.views import generic
from django.contrib import messages
from ..forms.subject_form import SubjectForm


def get(request, id):
    subject = get_object_or_404(SubjectModel, id=id)
    return render(request, 'subjects/index.html', {'subject': subject})


def get_all(request):
    subjects = SubjectModel.objects.all()
    return render(request, 'subjects/index.html', {'subjects': subjects, "test": "tests"})


@csrf_exempt
def create(request):
    print("create")
    # data = request.POST.dict()
    # new_subject = SubjectModel.objects.create(**data)

    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            data = request.POST.dict()
            form.save()
            messages.success(request, "La matière {} à été créée.".format(data['name']))
        else:
            messages.error(
                request, 'There are errors in the form please check')
    else:

        form = SubjectForm()

    context = {
        'form': form
    }
    print(context)
    return render(request, 'subjects/create.html', context)


@csrf_exempt
def update(request, id):
    data = request.POST.dict()
    SubjectModel.objects.filter(pk=id).update(**data)
    return redirect('subject_get', id)


@csrf_exempt
def delete(request, id):
    SubjectModel.objects.filter(pk=id).delete()
    return redirect('subject_get_all')
