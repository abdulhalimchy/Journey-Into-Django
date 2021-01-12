from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index(request):

    if request.user.is_authenticated:
        # authenticated users.
        return render(request, 'index.html')
    else:
        # anonymous users.
        return redirect('/login')

    

def loginUser(request):

    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        #match username & password with database
        user = authenticate(username=username, password=password)
        if user is not None:
            #A backend authenticated the credentials
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Incorrect username or password!')
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')