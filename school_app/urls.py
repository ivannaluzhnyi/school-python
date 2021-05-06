from django.urls import path, include

from . import views
from .views import index_views, subject_views, class_views, note_views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', login_required(index_views.HomePageView.as_view()), name='index'),
    path('accounts/', include('django.contrib.auth.urls'),),
    path('accounts/signup', index_views.SignUpView.as_view(), name='signup'),

    # Subject
    path('subject', subject_views.get_all, name='subject_get_all'),
    path('subject/<int:id>', subject_views.get, name='subject_get'),
    path('subject/create/', subject_views.create, name='subject_create'),
    path('subject/update/<int:id>', subject_views.update, name='subject_update'),
    path('subject/delete/<int:id>', subject_views.delete, name='subject_delete'),

    # Class
    path('class/', class_views.get_all, name='class_get_all'),
    path('class/<int:id>', class_views.get, name='class_get'),
    path('class/filter/<int:id>', class_views.get_all_filter_by_subject, name='class_get_filters'),
    path('class/create', class_views.create, name='class_create'),
    path('class/update/<int:id>', class_views.update, name='class_update'),
    path('class/delete/<int:id>', class_views.delete, name='class_delete'),

    # Notes
    path('notes', note_views.get_all, name="index_notes"),
    path('notes/update/<int:note_id>', note_views.update_view, name="update_note"),
    path('notes/delete/<int:note_id>', note_views.delete, name="delete_note")
]
