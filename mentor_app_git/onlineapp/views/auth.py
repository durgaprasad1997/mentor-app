from django.views import View
from onlineapp.forms.auth import *
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=SignUpForm
        return render(
            request,
            'signup.html',
            {'form':form,'title':'Sign Up|Online App'}
        )

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)

            user = authenticate(
                request,
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password']
            )

            if user is not None:
                login(request, user)
                return redirect('onlineapp:colleges')
            else:
                messages.error(request, 'Invalid Credentials')

            return redirect('login')


class LoginView(View):
    def get(self,request,*args,**kargs):
        login =  LoginForm
        return render(
            request,
            template_name="login.html",
            context={'form':login,'title':'Login Form'}
        )

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if user is not None:
                login(request,user)
                return redirect('onlineapp:colleges')
            else:
                messages.error(request,"Invalid Credentials")
                return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('onlineapp:login')