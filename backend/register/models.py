from django.db import models


DEPARTAMENTO_CHOICES = (
    ('fiscal', 'Fiscal'),
    ('rh', 'RH'),
    ('ti', 'TI'),
    ('vendas', 'Vendas'),
    ('financeiro', 'Financeiro'),
    ('producao', 'Produção'),
    ('marketing', 'Marketing'),
    ('logistica', 'Logística'),
)

FUNCAO_CHOICES = (
    ('gerente', 'Gerente'),
    ('analista', 'Analista'),
    ('desenvolvedor', 'Desenvolvedor'),
    ('coordenador', 'Coordenador'),
    ('assistente', 'Assistente'),
    ('estagiario', 'Estagiário'),
)


class Pessoa(models.Model):
    id = models.BigAutoField(primary_key=True)
    registro = models.IntegerField(blank=True, null=True)
    nome = models.CharField(max_length=150)
    departamento = models.CharField(max_length=30, choices=DEPARTAMENTO_CHOICES)
    funcao = models.CharField(max_length=30, choices=FUNCAO_CHOICES)
    data_registro = models.DateField(blank=True, null=True)


class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    DateOfJoining = models.DateField()

    def __str__(self):
        return self.EmployeeName





