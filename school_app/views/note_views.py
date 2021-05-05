from django.shortcuts import (get_object_or_404,
                              render,
                              redirect)
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from ..models import Note as NoteModel

def get(request, id):
    _note = get_object_or_404(NoteModel, id=id)
    return HttpResponse(_class)


def get_all(request):
    _notes = NoteModel.objects.all()
    user = request.user
    groups = list()
    for g in user.groups.all():
        groups.append(g)

    if "professor" in groups or "coordinator" in groups:
        role = "manager"
    role = "manager"
    return render(request, "pages/notes/index.html", { "notes": _notes, "role": role })



@csrf_exempt
def create(request):
    data = request.POST.dict()
    new_note = NoteModel.objects.create(**data)
    id = new_note.id
    return redirect('note_get', id)


@csrf_exempt
def update(request, id):
    data = request.POST.dict()
    NoteModel.objects.filter(pk=id).update(**data)
    return redirect('note_get', id)


@csrf_exempt
def delete(request, id):
    NoteModel.objects.filter(pk=id).delete()
    return redirect('note_get_all')