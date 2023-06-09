from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from register.models import Pessoa
from register.serializers import PessoaSerializer

from django.core.files.storage import default_storage


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
