from django.shortcuts import (get_object_or_404,
                              render,
                              redirect)
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from ..models import Class as ClassModel
from django.contrib import messages
from ..forms.class_form import ClassForm


def get(request, id):
    _class = get_object_or_404(ClassModel, id=id)
    return render(request, "pages/classes/read.html", {"class": _class})


def get_all(request):

    _classes = ClassModel.objects.prefetch_related(
        "subject").prefetch_related("user").all()

    user = request.user
    groups = list()
    for g in user.groups.all():
        groups.append(g)

    if "professor" in groups or "coordinator" in groups:
        role = "manager"
    role = "manager"

    return render(request, "pages/classes/index.html", {"classes": _classes, "role": role})


@csrf_exempt
def create(request):

    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            data = request.POST.dict()
            form.save()
            messages.success(
                request, "La class {} à été créée.".format(data['name']))
        else:
            messages.error(
                request, 'Il y a des erreurs dans le formulaire, veuillez vérifier')
    else:

        form = ClassForm()

    context = {
        'form': form,
        'title': "Créer une class"
    }
    return render(request, 'pages/classes/manage.html', context)


@csrf_exempt
def update(request, id):
    _class = ClassModel.objects.get(pk=id)
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            data = request.POST.dict()
            form.save()
            messages.success(
                request, "La class {} à bien été modifiée".format(data['name']))
        else:
            messages.error(
                request, 'Il y a des erreurs dans le formulaire, veuillez vérifier')
    else:
        form = ClassForm(instance=_class)
    return render(request, 'pages/classes/manage.html', {
        'form': form,
        'mode': "U",
        "title": "Mettre à jour une classe"
    })


@csrf_exempt
def delete(request, id):
    ClassModel.objects.filter(pk=id).delete()
    messages.success(request, "La classe à bien été surprimée.")
    return redirect('class_get_all')
