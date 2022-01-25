from rest_framework.validators import UniqueTogetherValidator
from rest_framework import serializers
from .models import *


class TurniejSerializer(serializers.HyperlinkedModelSerializer):
    mecze = serializers.HyperlinkedRelatedField(many=True, view_name='rozgrywka-detail', read_only=True)

    class Meta:
        model = Turniej
        fields = ['url', 'id', 'nazwa', 'miasto', 'ulica', 'nr_budynku', 'data', 'mecze']


class UczestnikSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Uczestnik
        fields = ['url', 'id', 'imie', 'nazwisko', 'nr_tel', 'nr_email', 'wiek']


class SedziaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Sedzia
        fields = ['url', 'id', 'imie', 'nazwisko']


class RozgrywkaSerializer(serializers.HyperlinkedModelSerializer):
    turniej = serializers.SlugRelatedField(queryset=Turniej.objects.all(), slug_field='nazwa')
    ucz1 = serializers.HyperlinkedRelatedField(queryset=Uczestnik.objects.all(), view_name='uczestnik-detail')
    ucz2 = serializers.HyperlinkedRelatedField(queryset=Uczestnik.objects.all(),view_name='uczestnik-detail')
    sedzia = serializers.HyperlinkedRelatedField(queryset=Sedzia.objects.all(), view_name='sedzia-detail')

    class Meta:
        model = Rozgrywka
        fields = ['url', 'id', 'turniej', 'ucz1', 'ucz2', 'sedzia', 'wynik_ucz1', 'wynik_ucz2']

