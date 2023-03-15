from django.shortcuts import render, HttpResponse

# Create your views here.
def login(request):
    return HttpResponse('Area Login')

def cadastro(request):
    return render(request, 'cadastro.html')

def logout(request):
    return HttpResponse('Area de logout')