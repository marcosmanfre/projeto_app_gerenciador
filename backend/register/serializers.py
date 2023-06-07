from rest_framework import serializers
from register.models import Employees, Pessoa

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees 
        fields=('EmployeeId','EmployeeName','Department','DateOfJoining')




class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pessoa
        fields=('id','nome','departamento','funcao','data_registro')