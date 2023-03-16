from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.models import User

# Create your views here.
def logar(request):
    return HttpResponse('Area Login')

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if len(username.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Não pode conter espaços em branco')
            return redirect('/auth/cadastro')

        if len(senha) < 5:
            messages.add_message(request, constants.ERROR, 'Sua senha tem que conter mais de 5 caracteres')
            return redirect('/auth/cadastro')
        
        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Usuário já existe')
            return redirect('/auth/cadastro')
        
        try:
            user = User(username=username, email=email, password=senha)

            user.save()
            messages.add_message(request, constants.SUCCESS, 'Usuário salvo com sucesso')
            return redirect('auth/cadastro')
        
        except:
            return redirect('/auth/cadastro')


def logout(request):
    return HttpResponse('Area de logout')