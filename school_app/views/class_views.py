from django.shortcuts import (get_object_or_404,
                              render,
                              redirect)
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, FileResponse, HttpResponseNotFound

from ..models import Class as ClassModel
from django.contrib import messages
from ..forms.class_form import ClassForm
from django.contrib.auth.decorators import login_required, permission_required


from django.core.files.storage import FileSystemStorage

from helpers import download_file


@login_required
def get(request, id):
    _class = get_object_or_404(ClassModel, id=id)
    _file = download_file.encode_path(_class.doc)
    filename = download_file.get_filename(_class.doc, "/")
    return render(request, "pages/classes/read.html", {"class": _class, "document": _file, "filename": filename})


@login_required
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


def get_all_filter_by_subject(request, id):
    _classes = ClassModel.objects.filter(subject=id)
    return render(request, "pages/classes/index.html", {"classes": _classes, "role": "manager"})


@login_required
@csrf_exempt
def create(request):

    if request.method == 'POST':
        form = ClassForm(request.POST, files=request.FILES)
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


@login_required
@csrf_exempt
def update(request, id):
    _class = ClassModel.objects.get(pk=id)

    if request.method == 'POST':
        form = ClassForm(request.POST, files=request.FILES, instance=_class)
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


@login_required
def doc_download(request, file_path):

    fs = FileSystemStorage()
    next_path = "/code/media/" + download_file.decode_path(file_path)
    filename = download_file.get_filename(file_path)

    if fs.exists(next_path):
        with fs.open(next_path) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="{}"'.format(
                filename)
            return response
    else:
        return HttpResponseNotFound('The requested pdf was not found in our server.')


@login_required
def delete(request, id):
    ClassModel.objects.filter(pk=id).delete()
    messages.success(request, "La classe à bien été surprimée.")
    return redirect('class_get_all')
