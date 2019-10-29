from rest_framework import viewsets

from testapp.models import Ocupacao, Referencia
from testapp.serializers import OcupacaoSerializer, ReferenciaSerializer


class OcupacaoViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que as ocupações sejam vistas e alteradas.
    """
    queryset = Ocupacao.objects.all().order_by('profissao')
    serializer_class = OcupacaoSerializer


class ReferenciaViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que as referências sejam vistas e alteradas
    """
    queryset = Referencia.objects.all()
    serializer_class = ReferenciaSerializer
