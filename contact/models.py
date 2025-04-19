from django.db import models

# Create your models here.
class Cadastros(models.Model):
    numero_apt = models.CharField(max_length=5)
    nome_morado = models.CharField(max_length=150)
    tipo_entrega = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome_morado