from rest_framework import serializers
from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    
    class Meta:
        # exibido somente quando for cadastrar
        # impede de deixar o email ser exibido ferindo a proteção de dado 
        extra_kwargs =  {
            'email' : {'write_only':True}
        }
        model = Avaliacao 
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )
        
        
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo'
        )