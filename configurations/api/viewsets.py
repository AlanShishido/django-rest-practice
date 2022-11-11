from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Cadastro, Comentario
from .serializers import CadastroSerializer, ComentarioSerializer


class CadastroViewSet(viewsets.ModelViewSet):
    # queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'idade', 'email']
    def get_queryset(self):
        print('get_queryset')
        ident = self.request.query_params.get('id', None)
        idade = self.request.query_params.get('idade', None)
        nome = self.request.query_params.get('nome', None)
        email = self.request.query_params.get('email', None)
        print((ident, idade, nome, email))
        queryset = Cadastro.objects.all()
        if ident:
            queryset = queryset.filter(pk=ident)
        if idade:
            queryset = queryset.filter(idade=idade)
        if nome:
            queryset = queryset.filter(name=nome)
        if email:
            queryset = queryset.filter(email=email)
        return queryset
    
    # GET METHOD
    def list(self, request, *args, **kwargs):
        print('list')
        return super(CadastroViewSet, self).list(request, *args, **kwargs)
        # return Response({'message': 'Ola mundo'})

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['email', 'avaliacao']
    
    # GET METHOD
    def list(self, request, *args, **kwargs):
        print('list')
        return super(ComentarioViewSet, self).list(request, *args, **kwargs)
    
    # POST METHOD
    def create(self, request, *args, **kwargs):
        print('create')
        return super(ComentarioViewSet, self).create(request, *args, **kwargs)

    # GET METHOD WITH Primary Key
    def retrieve(self, request, *args, **kwargs):
        print('retrieve')
        return super(ComentarioViewSet, self).retrieve(request, *args, **kwargs)

    # PUT METHOD'
    def update(self, request, *args, **kwargs):
        print('update')
        return super(ComentarioViewSet, self).update(request, *args, **kwargs)

    # PATCH METHOD
    def partial_update(self, request, *args, **kwargs):
        print('partial_update')
        return super(ComentarioViewSet, self).partial_update(request, *args, **kwargs)

    # DELETE METHOD
    def destroy(self, request, *args, **kwargs):
        print('destroy')
        return super(ComentarioViewSet, self).destroy(request, *args, **kwargs)

    # METODO DIFERENTE DO PADRAO COM ROTA NOVA
    @action(methods=['get'], detail=False)
    def olamundo(self, request):
        print('olamundo')
        return Response({'message': 'Hello World'})
    
    # METODO DIFERENTE DO PADRAO COM ROTA NOVA
    @action(methods=['get'], detail=True)
    def olamundocompk(self, request, pk=None):
        print('olamundocompk')
        return Response({'message': 'Hello World com Primary Key'})
