from django_filters import DateTimeFilter, NumberFilter, FilterSet
from rest_framework.response import Response
from rest_framework import generics
from .serializers import *
from rest_framework.reverse import reverse


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request):
        return Response({'turnieje': reverse(TurniejList.name, request=request),
                         'rozgrywki': reverse(RozgrywkaList.name, request=request),
                         'uczestnicy': reverse(UczestnikList.name, request=request),
                         'sedziowie': reverse(SedziaList.name, request=request)
                         })


class TurniejDateFilter(FilterSet):
    start_date = DateTimeFilter(field_name='data', lookup_expr='gte')
    end_date = DateTimeFilter(field_name='data', lookup_expr='lte')

    class Meta:
        model = Turniej
        fields = ['start_date', 'end_date', 'miasto']


class TurniejList(generics.ListCreateAPIView):
    queryset = Turniej.objects.all()
    serializer_class = TurniejSerializer
    name = 'turniej-list'
    filter_class = TurniejDateFilter
    ordering_fields = ['nazwa']


class TurniejDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Turniej.objects.all()
    serializer_class = TurniejSerializer
    name = 'turniej-detail'


class RozgrywkaList(generics.ListCreateAPIView):
    queryset = Rozgrywka.objects.all()
    serializer_class = RozgrywkaSerializer
    name = 'rozgrywka-list'
    filter_fields = ['ucz1', 'ucz2', 'sedzia']
    ordering_fields = ['ucz1']


class RozgrywkaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rozgrywka.objects.all()
    serializer_class = RozgrywkaSerializer
    name = 'rozgrywka-detail'


class UczestnikWiekFilter(FilterSet):
    start_wiek = NumberFilter(field_name='wiek', lookup_expr='gte')
    end_wiek = NumberFilter(field_name='wiek', lookup_expr='lte')

    class Meta:
        model = Uczestnik
        fields = ['start_wiek', 'end_wiek', 'imie', 'nazwisko']


class UczestnikList(generics.ListCreateAPIView):
    queryset = Uczestnik.objects.all()
    serializer_class = UczestnikSerializer
    name = 'uczestnik-list'
    filter_class = UczestnikWiekFilter
    ordering_fields = ['nazwisko', 'wiek']


class UczestnikDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Uczestnik.objects.all()
    serializer_class = UczestnikSerializer
    name = 'uczestnik-detail'


class SedziaList(generics.ListCreateAPIView):
    queryset = Sedzia.objects.all()
    serializer_class = SedziaSerializer
    name = 'sedzia-list'
    filter_fields = ['imie', 'nazwisko']
    ordering_fields = ['nazwisko']


class SedziaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sedzia.objects.all()
    serializer_class = SedziaSerializer
    name = 'sedzia-detail'
