from django.shortcuts import (get_object_or_404,
                              render,
                              redirect)
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from ..models import Subject as SubjectModel
from django.contrib import messages
from ..forms.subject_form import SubjectForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def get(request, id):
    subject = get_object_or_404(SubjectModel, id=id)
    return render(request, 'subjects/index.html', {'subject': subject})


def get_all(request):
    subjects = SubjectModel.objects.all().order_by('id')
    return render(request, 'subjects/index.html', {'subjects': subjects})


def create(request):

    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            data = request.POST.dict()
            form.save()
            messages.success(
                request, "La matière {} à été créée.".format(data['name']))
        else:
            messages.error(
                request, 'Il y a des erreurs dans le formulaire, veuillez vérifier')
    else:

        form = SubjectForm()

    context = {
        'form': form,
        'title': "Créer une matière"
    }
    return render(request, 'subjects/form.html', context)


@csrf_exempt
def update(request, id):
    subject = get_object_or_404(SubjectModel, id=id)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            data = request.POST.dict()
            form.save()
            messages.success(
                request, "La matière {} à été créée.".format(data['name']))
        else:
            messages.error(
                request, 'Il y a des erreurs dans le formulaire, veuillez vérifier')
    else:
        form = SubjectForm(instance=subject)

    context = {
        'form': form,
        'title': "Mettre à jour une matière"
    }
    return render(request, 'subjects/form.html', context)


def delete(request, id):
    SubjectModel.objects.filter(pk=id).delete()
    messages.success(request, "La matière à bien été surprimée.")
    return redirect('subject_get_all')
