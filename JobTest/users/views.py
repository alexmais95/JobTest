from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from .form import LogForm, RegistForm



def login_viev(request):
    if request.method == 'POST':
        form = LogForm(request.POST)
        
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user: 
                login(request, user)
                return HttpResponseRedirect(reverse('board:game'))
    
    else:
        form = LogForm

    return render(request, 'users/auth.html', {'form': form})


def registration_viev(request):
    if request.method == 'POST':
        form = RegistForm(request.POST)
        
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            
            
            return HttpResponseRedirect(reverse('users:login'))
            
    
    else:
        form = RegistForm

    return render(request, 'users/regist.html', {'form': form})


def logout_viev(request):
    logout(request)
    print('user_logout')
    return HttpResponseRedirect(reverse('users:login'))
   
