from django import forms 
from django.core.exceptions import ValidationError
from . import models


class CadastroForm(forms.ModelForm):
    numero_apt = forms.CharField(
        widget=forms.TimeInput(
            attrs={
                'placeholder':'Digite o numero',
            }
        ),
        help_text='Numero do apartamento',
    )
    motivos = forms.CharField(
        widget=forms.TimeInput(
            attrs={
                'placeholder':'Digite o numero',
            }
        ),
        help_text='Numero do apartamento',
    )
    nome_morado = forms.CharField(
        widget=forms.TimeInput(
            attrs={
                'placeholder':'Digite o destino',
            }
        ),
        help_text='Nome do Proprietario',
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    class Meta:
        model = models.Cadastros
        fields = (
            'numero_apt', 'nome_morado'
        )