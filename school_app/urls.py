from django.urls import path, include

from . import views
from .views import SignUpView

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name="test"),
    path('accounts/', include('django.contrib.auth.urls'),),
    path('accounts/signup', SignUpView.as_view(), name='signup'),
    path('home/', HomePageView.as_view(), name='home'),
]
