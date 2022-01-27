from django_filters import DateTimeFilter, NumberFilter, FilterSet
from rest_framework.response import Response
from rest_framework import generics
from .serializers import *
from rest_framework.reverse import reverse
from rest_framework import permissions

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
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = Turniej.objects.all()
    serializer_class = TurniejSerializer
    name = 'turniej-list'
    filter_class = TurniejDateFilter
    ordering_fields = ['nazwa']
    search_fields = ['nazwa']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TurniejDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = Turniej.objects.all()
    serializer_class = TurniejSerializer
    name = 'turniej-detail'


class RozgrywkaList(generics.ListCreateAPIView):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = Rozgrywka.objects.all()
    serializer_class = RozgrywkaSerializer
    name = 'rozgrywka-list'
    filter_fields = ['ucz1', 'ucz2', 'sedzia']
    ordering_fields = ['ucz1']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RozgrywkaDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
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
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Uczestnik.objects.all()
    serializer_class = UczestnikSerializer
    name = 'uczestnik-list'
    filter_class = UczestnikWiekFilter
    ordering_fields = ['nazwisko', 'wiek']
    search_fields = ['imie', 'nazwisko']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UczestnikDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Uczestnik.objects.all()
    serializer_class = UczestnikSerializer
    name = 'uczestnik-detail'


class SedziaList(generics.ListCreateAPIView):
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Sedzia.objects.all()
    serializer_class = SedziaSerializer
    name = 'sedzia-list'
    filter_fields = ['imie', 'nazwisko']
    ordering_fields = ['nazwisko']
    search_fields = ['imie', 'nazwisko']


class SedziaDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Sedzia.objects.all()
    serializer_class = SedziaSerializer
    name = 'sedzia-detail'
