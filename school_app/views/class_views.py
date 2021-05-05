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
    return HttpResponse(_class)


def get_all(request):
    _class = ClassModel.objects.all()
    return HttpResponse(_class)


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
        'form': form
    }
    return render(request, 'class/create.html', context)


@csrf_exempt
def update(request, id):
    data = request.POST.dict()
    ClassModel.objects.filter(pk=id).update(**data)
    return redirect('class_get', id)


@csrf_exempt
def delete(request, id):
    ClassModel.objects.filter(pk=id).delete()
    return redirect('class_get_all')
