from django.shortcuts import render, redirect
from contact.models import *
from django.urls import reverse
from contact.forms import *
from django.contrib import messages

def index(request):
    return render (
        request, 
        'global/base.html',
    )

def cadastros(request):
    form_action = reverse('contact:cadastros')
    if request.method == 'POST':
        form_cadastro = CadastroForm(request.POST)
        context = {
            'form': form_cadastro,
            'form_action': form_action,
        }

        if form_cadastro.is_valid():
            form_cadastro.save()
            messages.success(request, 'Cadastro registrado com sucesso !!!')
            return redirect('contact:visualizacao')
        
        return render (
            request, 
            'contact/cadastra.html',
            context,
        )
    context = {
            'form': CadastroForm(),
            'form_action': form_action,
        }

    return render (
        request, 
        'contact/cadastra.html',
        context,
    )

def visualizacao(request):

    registro = Cadastros.objects.filter().order_by('-id')

    context = {
        'registro': registro,
    }

    return render(
        request,
        'contact/index.html',
        context,
    )