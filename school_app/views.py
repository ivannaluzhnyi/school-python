from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

def index(request):
    return HttpResponse("Hello, world. You're at the school_app index.")

def test(request):
    return render(
        request, 
        "test.html",
        {
            "test" : "rémi"
        }
    )

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'