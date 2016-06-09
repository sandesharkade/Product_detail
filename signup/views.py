from django.shortcuts import render
from .forms import SignupForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.views.generic import TemplateView, FormView


class Register_user(FormView):

    def get(self, request):
        user_form = SignupForm
        return render(request, 'signup/register.html', {'user_form': user_form})

    def post(self, request):
        registered = False  # to tell if the registration was successfull or not
        form = SignupForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            return HttpResponseRedirect('/')

        else:
            return render(request,'signup/register.html', {'user_form': form})

class Login_view(TemplateView):

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('product')
        else:
            msg = "Wrong Username OR Wrong Password"
            return render(request,'signup/login.html', {'msg': msg})
# Create your views here.
