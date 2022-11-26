from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def registration(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return render(request, 'registration.html', {'error1':True})
        if User.objects.filter(username=uname).exists():
            return render(request, 'registration.html', {'error2':True})
        else:
            newuser = User.objects.create_user(username=uname, first_name=fname, last_name=lname, email=email, password=pass1)
            newuser.save()
            return redirect('loginPage')

    return render(request, 'registration.html')

def loginPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pass1 = request.POST.get('password')

        user = authenticate(request, username=uname, password=pass1)

        if user is not None:
            login(request, user)
            return redirect('homePage')
        else:
            print('Dont Login!')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('loginPage')

def homePage(request):
    return render(request, 'home.html')