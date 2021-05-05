from django.shortcuts import (get_object_or_404,
                              render,
                              redirect)
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from ..models import Class as ClassModel

def get(request, id):
    _class = get_object_or_404(ClassModel, id=id)
    return HttpResponse(_class)


def get_all(request):
    _class = ClassModel.objects.all()
    return render(request, "pages/notes/index.html", { "classes": _class })


@csrf_exempt
def create(request):
    data = request.POST.dict()
    new_class = ClassModel.objects.create(**data)
    id = new_class.id
    return redirect('class_get', id)


@csrf_exempt
def update(request, id):
    data = request.POST.dict()
    ClassModel.objects.filter(pk=id).update(**data)
    return redirect('class_get', id)


@csrf_exempt
def delete(request, id):
    ClassModel.objects.filter(pk=id).delete()
    return redirect('class_get_all')