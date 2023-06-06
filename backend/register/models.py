from django.db import models
from djongo import models as djmodels

class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    registro = models.CharField(max_length=25, blank=True, null=True)
    nome = models.CharField(max_length=150)
    departamento = models.CharField(max_length=30,)
    funcao = models.CharField(max_length=30, blank=True, null=True)



    def __str__(self):
        return self.nome