from rest_framework import serializers
from register.models import Pessoa


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pessoa
        fields = '__all__'