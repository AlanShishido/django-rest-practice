from rest_framework import serializers
from ..models import Cadastro, Comentario

class CadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadastro
        fields = ('name', 'idade', 'email')

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ('email', 'avaliacao', 'comentario')
