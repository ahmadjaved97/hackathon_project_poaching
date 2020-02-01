from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('alerts')
        else:
            messages.info(request, 'Username OR password is not correct')
    
    context = {}
    return render(request, 'users/login.html', context)



def logoutUser(request):
    logout(request)
    return redirect('login')