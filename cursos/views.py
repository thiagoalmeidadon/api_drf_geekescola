from django.db.models.fields import mixins
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from .models import Curso, Avaliacao 
from .serializers import CursoSerializer, AvaliacaoSerializer

from rest_framework import viewsets
from rest_framework.decorators import action  
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import permissions
from .permissions import EhSuperUser

""" API V1 """
# ListCreateAPIView lista e cria 
# RetrieveUpdateDestroyAPIView é implementado de outra forma e continua a ação do CRUD
class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    
    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(), curso_id=self.kwargs.get('curso_pk'), pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))
    
class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    
    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
        return self.queryset.all()
    

""" APi V2 """

class CursoViewSet(viewsets.ModelViewSet):
    permission_classes = (
        EhSuperUser,
        permissions.DjangoModelPermissions,
    )
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        # paginação global do DRF não influencia no método sobreescrito
        # é necessario implementar manualmente 
        self.pagination_class.page_size = 1
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page = self.paginate_queryset(avaliacoes)
        
        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginate_response(serializer.data)
        
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)
    
"""    
class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
"""

# customizando viewset 
class AvaliacaoViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer