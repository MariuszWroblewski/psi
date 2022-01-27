from rest_framework.validators import UniqueTogetherValidator
from rest_framework import serializers
from .models import *
from datetime import date


class TurniejSerializer(serializers.HyperlinkedModelSerializer):
    mecze = serializers.HyperlinkedRelatedField(many=True, view_name='rozgrywka-detail', read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Turniej
        fields = ['url', 'id', 'nazwa', 'miasto', 'ulica', 'nr_budynku', 'data', 'owner', 'mecze']

    def validate_data(self, data):
        if data < date.today():
            raise serializers.ValidationError("Błedna data. Data nie może być wcześniejsza niż obecna")
        return data


class UczestnikSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Uczestnik
        fields = ['url', 'id', 'imie', 'nazwisko', 'nr_tel', 'nr_email', 'wiek', 'owner']

    def validate_wiek(self, wiek):
        if wiek < 5 or wiek > 100:
            raise serializers.ValidationError("Podano blędną wartość. Minimalny wiek to 5 lat, maksymalny 100")
        return wiek


class SedziaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Sedzia
        fields = ['url', 'id', 'imie', 'nazwisko']


class RozgrywkaSerializer(serializers.HyperlinkedModelSerializer):
    turniej = serializers.SlugRelatedField(queryset=Turniej.objects.all(), slug_field='nazwa')
    ucz1 = serializers.HyperlinkedRelatedField(queryset=Uczestnik.objects.all(), view_name='uczestnik-detail')
    ucz2 = serializers.HyperlinkedRelatedField(queryset=Uczestnik.objects.all(),view_name='uczestnik-detail')
    sedzia = serializers.HyperlinkedRelatedField(queryset=Sedzia.objects.all(), view_name='sedzia-detail')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Rozgrywka
        fields = ['url', 'id', 'turniej', 'ucz1', 'ucz2', 'sedzia', 'wynik_ucz1', 'wynik_ucz2', 'owner']

    def validate_wynik_ucz1(self, wynik_ucz1):
        if wynik_ucz1 < 0 or wynik_ucz1 > 5:
            raise serializers.ValidationError("Błedny wynik, możliwy wynik jest z zakresu 0-5")
        return wynik_ucz1

    def validate_wynik_ucz2(self, wynik_ucz2):
        if wynik_ucz2 < 0 or wynik_ucz2 > 5:
            raise serializers.ValidationError("Błedny wynik, możliwy wynik jest z zakresu 0-5")
        return wynik_ucz2
