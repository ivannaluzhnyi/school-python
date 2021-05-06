from django.shortcuts import (get_object_or_404,
                              render,
                              redirect)
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib import messages
from ..models import Note as NoteModel
from ..forms.note_form import NoteForm
from django.contrib.auth.decorators import login_required
@login_required
def get(request, id):
    _note = get_object_or_404(NoteModel, id=id)
    return HttpResponse(_class)

@login_required
def get_all(request):
    _notes = NoteModel.objects.all().order_by('id')
    user = request.user
    groups = list()
    for g in user.groups.all():
        groups.append(g)

    if "professor" in groups or "coordinator" in groups:
        role = "manager"
    role = "manager"
    return render(request, "pages/notes/index.html", { "notes": _notes, "role": role })


@login_required
def create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            data = request.POST.dict()
            note = form.save()
            messages.success(
                request, "La note {} à bien été créée pour l'utilisateur {}".format(data['note'], note.user.username))
        else:
            messages.error(
                request, 'Il y a des erreurs dans le formulaire, veuillez vérifier')
    else:

        form = NoteForm(user_id=request.user.id)

    return render(request, 'pages/notes/manage.html', {
        'form': form
    })

@login_required
def update_view(request, note_id):
    _note = NoteModel.objects.get(pk=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=_note)
        if form.is_valid():
            data = request.POST.dict()
            form.save()
            messages.success(
                request, "La note {} à bien été modifiée".format(data['id']))
        else:
            messages.error(
                request, 'Il y a des erreurs dans le formulaire, veuillez vérifier')
    else:
        form = NoteForm(instance=_note)
    return render(request, 'pages/notes/manage.html', {
        'form': form
    })



@login_required
def delete(request, note_id):
    NoteModel.objects.filter(pk=note_id).delete()
    messages.success(request, "La note à bien été surprimée.")
    return redirect('index_notes')