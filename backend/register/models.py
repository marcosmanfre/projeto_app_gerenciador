from django.db import models


DEPARTAMENT_CHOICES = (
    ('Fiscal', 'Fiscal'),
    ('RH', 'RH'),
    ('TI', 'TI'),
    ('Vendas', 'Vendas'),
    ('Financeiro', 'Financeiro'),
    ('Produção', 'Produção'),
    ('Marketing', 'Marketing'),
    ('Logística', 'Logística'),
)

ROLE_CHOICES = (
    ('Gerente', 'Gerente'),
    ('Analista', 'Analista'),
    ('Desenvolvedor', 'Desenvolvedor'),
    ('Coordenador', 'Coordenador'),
    ('Assistente', 'Assistente'),
    ('Estagiário', 'Estagiário'),
)


class Employees(models.Model):
    EmployeeId = models.BigAutoField(primary_key=True)
    Register = models.IntegerField(blank=True, null=True)
    EmployeeName = models.CharField(max_length=500)
    Department = models.CharField(max_length=30, choices=DEPARTAMENT_CHOICES)
    Role = models.CharField(max_length=30, choices=ROLE_CHOICES)
    DateOfJoining = models.DateField()

    def __str__(self):
        return self.EmployeeName





