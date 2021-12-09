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
     
    # é um padrão de validação no serialize usar validade_    
    def validade_avaliacao(self, valor):
        if valor in range(1,6):
            return valor
        raise serializers.ValidationError("valor fora do range")
        
        
        
class CursoSerializer(serializers.ModelSerializer):
    # Nested Relationship
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    
    # Hyperlinked Related Field 
    #avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="avaliacao-detail")
    
    # Primary Key Related Field 
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo', 
            'avaliacoes'
        )