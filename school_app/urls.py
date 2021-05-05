from django.urls import path, include

from . import views
from .views import SignUpView, HomePageView

urlpatterns = [
    path('test/', views.test, name="test"),
    path('accounts/', include('django.contrib.auth.urls'),),
    path('accounts/signup', SignUpView.as_view(), name='signup'),
    path('', HomePageView.as_view(), name='index'),
]
