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


class TurniejList(generics.ListCreateAPIView):
    queryset = Turniej.objects.all()
    serializer_class = TurniejSerializer
    name = 'turniej-list'


class TurniejDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Turniej.objects.all()
    serializer_class = TurniejSerializer
    name = 'turniej-detail'


class RozgrywkaList(generics.ListCreateAPIView):
    queryset = Rozgrywka.objects.all()
    serializer_class = RozgrywkaSerializer
    name = 'rozgrywka-list'


class RozgrywkaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rozgrywka.objects.all()
    serializer_class = RozgrywkaSerializer
    name = 'rozgrywka-detail'


class UczestnikList(generics.ListCreateAPIView):
    queryset = Uczestnik.objects.all()
    serializer_class = UczestnikSerializer
    name = 'uczestnik-list'


class UczestnikDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Uczestnik.objects.all()
    serializer_class = UczestnikSerializer
    name = 'uczestnik-detail'


class SedziaList(generics.ListCreateAPIView):
    queryset = Sedzia.objects.all()
    serializer_class = SedziaSerializer
    name = 'sedzia-list'


class SedziaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sedzia.objects.all()
    serializer_class = SedziaSerializer
    name = 'sedzia-detail'