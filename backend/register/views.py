from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from register.models import Employees, Pessoa
from register.serializers import EmployeeSerializer, PessoaSerializer

from django.core.files.storage import default_storage


@csrf_exempt
def employeeApi(request,id=0):
    if request.method=='GET':
        employees = Employees.objects.all()
        employees_serializer=EmployeeSerializer(employees,many=True)
        return JsonResponse(employees_serializer.data,safe=False)
    
    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employees_serializer=EmployeeSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Adicionado com sucesso",safe=False)
        return JsonResponse("Erro ao adicionar",safe=False)
    
    elif request.method=='PUT':
        employee_data=JSONParser().parse(request)
        employee=Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        employees_serializer=EmployeeSerializer(employee,data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Atualizado com sucesso",safe=False)
        return JsonResponse("Erro ao atualizar")
    
    elif request.method=='DELETE':
        employee=Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deletado com sucesso",safe=False)


@csrf_exempt
def pessoaApi(request, id=0):
    if request.method == 'GET':
        pessoa = Pessoa.objects.all()
        pessoa_serializer = PessoaSerializer(pessoa, many=True)
        return JsonResponse(pessoa_serializer.data, safe=False)
    
    elif request.method == 'POST':
        pessoa_data = JSONParser().parse(request)
        pessoa_serializer = PessoaSerializer(data=pessoa_data)
        if pessoa_serializer.is_valid():
            pessoa_serializer.save()
            return JsonResponse("Adicionado com sucesso", safe=False)
        return JsonResponse("Erro ao adicionar", safe=False)
    
    elif request.method == 'PUT':
        pessoa_data = JSONParser().parse(request)
        pessoa = Pessoa.objects.get(id=pessoa_data['id'])
        pessoa_serializer = PessoaSerializer(pessoa, data=pessoa_data)
        if pessoa_serializer.is_valid():
            pessoa_serializer.save()
            return JsonResponse("Atualizado com sucesso", safe=False)
        return JsonResponse("Erro ao atualizar")
    
    elif request.method == 'DELETE':
        pessoa = Pessoa.objects.get(id=id)
        pessoa.delete()
        return JsonResponse("Deletado com sucesso", safe=False)
