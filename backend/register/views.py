from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


from register.models import Pessoa
from register.serializers import PessoaSerializer
from django.core.files.storage import default_storage
from django.http import JsonResponse


    
@csrf_exempt
def pessoaApi(request, obj_id=None):
    if request.method == 'GET':
        if obj_id:
            pessoa = Pessoa.objects.filter(pk=obj_id).first()
            if not pessoa:
                return JsonResponse(f'Pessoa com o ID {obj_id} não existe.', status=404, safe=False)
            pessoa_serializer = PessoaSerializer(pessoa)
            return JsonResponse(pessoa_serializer.data, safe=False)
        else:
            pessoas = Pessoa.objects.all()
            pessoa_serializer = PessoaSerializer(pessoas, many=True)
            return JsonResponse(pessoa_serializer.data, safe=False)
    

    elif request.method == 'POST':
        pessoa_data = JSONParser().parse(request)
        pessoa_serializer = PessoaSerializer(data=pessoa_data)
        if pessoa_serializer.is_valid():
            pessoa_serializer.save()
            return JsonResponse(pessoa_serializer.data, status=201, safe=False)
        return JsonResponse(pessoa_serializer.errors, status=400, safe=False)
    
    elif request.method == 'PUT':
        if not obj_id:
            return JsonResponse('O ID da pessoa é necessário para realizar operação.', status=400, safe=False)
        pessoa = Pessoa.objects.filter(pk=obj_id).first()
        if not pessoa:
            return JsonResponse(f'Pessoa com o ID {obj_id} não existe.', status=404, safe=False)
        pessoa_data = JSONParser().parse(request)
        pessoa_serializer = PessoaSerializer(pessoa, data=pessoa_data)
        if pessoa_serializer.is_valid():
            pessoa_serializer.save()
            return JsonResponse(pessoa_serializer.data, status=200, safe=False)
        return JsonResponse(pessoa_serializer.errors, status=400, safe=False)
    
    elif request.method == 'DELETE':
        if not obj_id:
            return JsonResponse('O ID da pessoa é necessário para realizar esta operação.', status=400, safe=False)
        pessoa = Pessoa.objects.filter(pk=obj_id).first()
        if not pessoa:
            return JsonResponse(f'Pessoa com o ID {obj_id} não existe.', status=404, safe=False)
        pessoa.delete()
        return JsonResponse('Pessoa deletada com sucesso.', status=204, safe=False)