from django.shortcuts import render
from .forms import SignupForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic import TemplateView, FormView


class Register_user(FormView):

    '''
    To add a user
    '''

    def get(self, request):
        user_form = SignupForm
        return render(request, 'signup/register.html',
                      {'user_form': user_form})

    def post(self, request):
        form = SignupForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/')

        else:
            return render(request, 'signup/register.html', {'user_form': form})


class Login_view(TemplateView):

    '''
    Login user code
    '''
    def get(self,request):
        if request.user.is_active:
            return HttpResponseRedirect('product')
        return render(request,'signup/login.html')


    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('product')
        else:
            msg = "Wrong Username OR Wrong Password"
            return render(request, 'signup/login.html', {'msg': msg})
