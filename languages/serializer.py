from rest_framework import serializers
from .models import Language,Paradign,Programer


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ('id','url','name','paradign')

class ParadignSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paradign
        fields = ('id','url','name')

class ProgramerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programer
        fields = ('id','url','name','language')