from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.core.files.storage import FileSystemStorage
# Create your views here.
def home(request):
    return render(request, 'home.html')


@login_required
def subir(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request,'subir.html',{
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'subir.html')
def exit(request):
    logout(request)
    return redirect('home')


def register(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        # se cargo los datos que llegan por el post y se lo tiene en el formulario
        user_creation_form = CustomUserCreationForm(data=request.POST)
        # Preguntamos si es valido lo que esta llegando
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'],
                                password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
    return render(request, 'registration/register.html', data)
