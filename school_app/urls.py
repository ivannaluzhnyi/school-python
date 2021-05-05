from django.urls import path, include

from .views import HomePageView

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls'),),
    path('home/', HomePageView.as_view(), name='home'),
]
