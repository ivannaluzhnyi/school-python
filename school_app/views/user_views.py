from django.shortcuts import (get_object_or_404,
                              render,
                              redirect)
from ..forms.profile_form import ProfilForm
from ..forms.user_form import UserForm
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User

def index(request):
    _users = User.objects.all().order_by('username')

    return render(request, "pages/users/index.html", { "users": _users })

def update_profile_view(request):
    user = request.user

    if request.method == 'POST':
        form = ProfilForm(request.POST, instance=user)
        if form.is_valid():
            data = request.POST.dict()
            form.save()
            messages.success(
                request, "L'utilisateur {} à bien été modifiée".format(data['username']))
        else:
            messages.error(
                request, 'Il y a des erreurs dans le formulaire, veuillez vérifier.')
    else:
        form = ProfilForm(instance=user)
    return render(request, 'pages/profil/edit.html', {
        'form': form,
    })

def create_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            data = request.POST.dict()
            note = form.save()
            messages.success(
                request, "La note {} à bien été créée pour l'utilisateur {}".format(data['note'], note.user.username))
        else:
            messages.error(
                request, 'Il y a des erreurs dans le formulaire, veuillez vérifier')
    else:

        form = UserForm()

    return render(request, 'pages/notes/manage.html', {
        'form': form,
        'mode': 'C'
    })