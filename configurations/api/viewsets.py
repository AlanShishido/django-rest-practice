from rest_framework import viewsets
from ..models import Cadastro, Comentario
from .serializers import CadastroSerializer, ComentarioSerializer


class CadastroViewSet(viewsets.ModelViewSet):
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer


class ComentarioViewSet(viewsets.ModelViewSet):
    serializer_class = ComentarioSerializer

    #alterar o query_set  no lugar do queryset = MODELO.objects.all()
    def get_queryset(self):
        return Comentario.objects.all()
    
    # GET METHOD
    # def list(self, request):
    #     pass
    
    # POST METHOD
    # def create(self, request):
    #     pass

    # GET METHOD WITH ID
    # def retrieve(self, request, pk=None):
    #     pass

    # PUT METHOD
    # def update(self, request, pk=None):
    #     pass

    # PATCH METHOD
    # def partial_update(self, request, pk=None):
    #     pass

    # DELETE METHOD
    # def destroy(self, request, pk=None):
    #     pass

