from django.core.validators import RegexValidator
from django.db import models


class Ocupacao(models.Model):
    profissao = models.CharField(max_length=128, blank=False, null=False)
    nome_empresa = models.CharField(max_length=255, blank=False, null=False)
    data_inicio = models.DateTimeField(
        auto_now=True, auto_now_add=False, blank=False, null=False)
    salario_liquido = models.DecimalField(max_digits=6,
                                          decimal_places=2, blank=False, null=False)


class Referencia(models.Model):
    nome = models.CharField(max_length=128)
    vinculo = models.CharField(max_length=100)
    celular_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    celular = models.CharField(
        validators=[celular_regex], max_length=13, blank=False, null=False)
    telefone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$')
    tel_residencial = models.CharField(
        validators=[telefone_regex], max_length=13, blank=False, null=False)
    tel_comercial = models.CharField(
        validators=[telefone_regex], max_length=13, blank=True, null=True)
    ocupacao = models.OneToOneField(
        Ocupacao, related_name='ocupacao', on_delete=models.CASCADE)
