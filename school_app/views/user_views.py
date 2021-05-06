from django.shortcuts import (get_object_or_404,
                              render,
                              redirect)
from ..forms.profile_form import ProfilForm
from ..forms.user_create_form import UserCreateForm
from ..forms.user_update_form import UserUpdateForm
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
        form = UserCreateForm(request.POST)
        if form.is_valid():
            data = request.POST.dict()
            form.clean()
            user = form.save()
            messages.success(
                request, "L'utilisateur {} à bien été créé.".format(user.username))
        else:
            messages.error(
                request, 'Il y a des erreurs dans le formulaire, veuillez vérifier')
    else:

        form = UserCreateForm()

    return render(request, 'pages/users/manage.html', {
        'form': form,
        'mode' : 'C'
    })

def update_view(request, user_id):
    _user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=_user)
        if form.is_valid():
            data = request.POST.dict()
            note = form.save()
            messages.success(
                request, "L'utilisateur {} à bien été modifié {}".format(data['username']))
        else:
            messages.error(
                request, 'Il y a des erreurs dans le formulaire, veuillez vérifier')
    else:

        form = UserUpdateForm(instance=_user)

    return render(request, 'pages/users/manage.html', {
        'form': form,
        'mode' : 'U'
    })

def delete(request, user_id):
    User.objects.filter(pk=user_id).delete()
    messages.success(request, "L'utilisateur à bien été supprimé).")
    return redirect('index_users')