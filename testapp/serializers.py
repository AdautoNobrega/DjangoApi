from rest_framework import serializers

from testapp.models import Ocupacao, Referencia


class OcupacaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ocupacao
        fields = ['profissao', 'nome_empresa',
                  'data_inicio', 'salario_liquido']


class OcupacaoListingField(serializers.RelatedField):
    def to_representation(self, value):
        return 'Ocupacao %d, %s' % (value[0], value[1])


class ReferenciaSerializer(serializers.HyperlinkedModelSerializer):
    ocupacao = OcupacaoListingField(
        queryset=Ocupacao.objects.all().values_list('id', 'profissao'), many=False)

    class Meta:
        model = Referencia
        fields = ['nome', 'vinculo', 'celular',
                  'tel_residencial', 'tel_comercial', 'ocupacao']
