from django.urls import path, include

from . import views
from .views import index_views, subject_views

urlpatterns = [
    path('', index_views.index, name='index'),
    path('test/', index_views.test, name="test"),
    path('accounts/', include('django.contrib.auth.urls'),),
    path('accounts/signup', index_views.SignUpView.as_view(), name='signup'),
    path('home/', index_views.HomePageView.as_view(), name='home'),

    # Subject
    path('subject', subject_views.get_all, name='subject_get_all'),
    path('subject/<int:id>', subject_views.get, name='subject_get'),
    path('subject/create/', subject_views.create, name='subject_create'),
    path('subject/update/<int:id>', subject_views.update, name='subject_update'),
    path('subject/delete/<int:id>', subject_views.delete, name='subject_delete'),

    # path('home1/', subject_views.SubjectListView.as_view(), name='suject_list'),
]
