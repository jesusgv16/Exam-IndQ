from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, get_user_model,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

from .forms import SignUpForm



@login_required
def home_view(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    return render('login_view')    
 

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)

            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    #CREAMOS UN FORMULARIO DE AUTENTICACION VACIO
    form = AuthenticationForm()
    if request.method == "POST":
        #añadimos los datos recibidos del formulario
        form=AuthenticationForm(data=request.POST)
        #si el formulario es valido...
        if form.is_valid():
            #recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #verificamos las credenciales del usuario
            user=authenticate(username=username, password=password)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            #si existe un usuario con ese nombre y contraseña
            if user is not None:
                #login manualmente
                login(request, user)
                #y si redirecciona a la portada
                return redirect('/')  
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')
