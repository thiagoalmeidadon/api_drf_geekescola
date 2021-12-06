from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

class CursoAPIView(APIView):
    """API de cursos"""
    def get(self, request):
        cursos = Curso.objects.all()
        #quando tem muitos passar o parametro many=
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)
    
    
class AvaliacaoAPIView(APIView):
    """API avaliação do curso""" 
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)
