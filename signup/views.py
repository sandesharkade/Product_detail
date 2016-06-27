from django.shortcuts import render
from .forms import SignupForm
from django.contrib.auth import authenticate, login                     
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.views.generic import TemplateView, FormView
from django.core.mail import EmailMessage

class Register_user(FormView):

    '''
    To add a user
    '''

    def post(self, request):
        form = SignupForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            email = EmailMessage('Registration for product blog site',
                                 'rohan9.pythonanywhere.com', to=[request.POST['email']])
            email.send()
            user.save()
            return HttpResponse(status=200)
        else:
            return HttpResponse(form.errors, status=400)


class Login_view(TemplateView):

    '''
    Login user code
    '''

    def get(self, request):
        if request.user.is_active:
            return HttpResponseRedirect('product')
        return render(request, 'signup/login.html')

    def post(self, request):
        username = request.POST['u_name']
        password = request.POST['login_password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)
            
