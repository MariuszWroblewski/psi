from rest_framework.test import APITestCase, APIClient
from django.test import TestCase
from rest_framework.reverse import reverse
from . import views
from .models import Turniej, Sedzia
from rest_framework import status
from django.contrib.auth.models import User

# Create your tests here.


class TurniejTests(APITestCase):

    def create_turniej(self, nazwa, miasto, ulica, nr_budynku, date, owner, client):
        url = reverse(views.TurniejList.name)
        data = {'nazwa': nazwa,
                'miasto': miasto,
                'ulica': ulica,
                'nr_budynku': nr_budynku,
                'data': date,
                'owner': owner
                }
        response = client.post(url, data, format='json')
        return response

    def test_post_and_get_turniej_unauthorized_user(self):
        user = User.objects.create_user('admin', 'admin@ad.com', 'admin1234')
        client = APIClient()
        client.login(username='admin', password='admin1234')
        nazwa = 'Nazwa turnieju'
        miasto = 'Warszawa'
        ulica = 'Olsztyńska'
        nr_budynku = '1A'
        date = 2023-10-12
        response = self.create_turniej(nazwa, miasto, ulica, nr_budynku, date, user.id, client)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TurniejTests2(TestCase):
    def setUp(self):
        self.item = Turniej.objects.create(
            nazwa='Turniej',
            miasto='Olsztyn',
            ulica='Olecka',
            nr_budynku='1',
            # data=2023-12-12
        )

    def test_turniej_creation(self):
        self.assertEqual(self.item.nazwa, 'Turniej')
        self.assertEqual(self.item.miasto, 'Olsztyn')
        self.assertEqual(self.item.ulica, 'Olecka')
        self.assertEqual(self.item.nr_budynku, '1')
        # self.assertEqual(self.item.data, 2023-12-12)

        self.assertIsInstance(self.item.nazwa, str)
        self.assertIsInstance(self.item.miasto, str)
        self.assertIsInstance(self.item.ulica, str)
        self.assertIsInstance(self.item.nr_budynku, str)

    def test_turniej_qty(self):
        item_count = Turniej.objects.all().count()
        self.assertEqual(item_count, 1)


class SedziaTests(APITestCase):

    def create_sedza(self, imie, nazwisko, client):
        url = reverse(views.TurniejList.name)
        data = {'imie': imie,
                'nazwisko': nazwisko,
                }
        response = client.post(url, data, format='json')
        return response

    def test_post_and_get_sedzia_unauthorized_user(self):
        user = User.objects.create_user('admin', 'admin@ad.com', 'admin1234')
        client = APIClient()
        client.login(username='admin', password='admin1234')
        imie = 'Jan'
        nazwisko = 'Nowak'
        response = self.create_sedza(imie, nazwisko, client)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class SedziaTest(TestCase):
    def setUp(self):
        self.item = Sedzia.objects.create(
            imie='Jan',
            nazwisko="Nowak"
        )

    def test_sedzia_creation(self):
        self.assertEqual(self.item.imie, 'Jan')
        self.assertEqual(self.item.nazwisko, 'Nowak')

        # self.assertTrue(self.item.imie == 'jan')
        # self.assertTrue(self.item.nazwisko == 'nowak')

        self.assertIsInstance(self.item.imie, str)
        self.assertIsInstance(self.item.nazwisko, str)
        # self.assertIsInstance(self.item.imie, int)
        # self.assertIsInstance(self.item.nazwisko, str)

    def test_sedzia_qty(self):
        item_count = Sedzia.objects.all().count()
        self.assertEqual(item_count, 1)


class UczestnikTests(APITestCase):

    def create_uczestnik(self, imie, nazwisko, wiek, client):
        url = reverse(views.UczestnikList.name)
        data = {'imie': imie,
                'nazwisko': nazwisko,
                'wiek': wiek,
                }
        response = client.post(url, data, format='json')
        return response

    def test_post_and_get_uczestnik_unauthorized_user(self):
        user = User.objects.create_user('admin', 'admin@ad.com', 'admin1234')
        client = APIClient()
        client.login(username='admin', password='admin1234')
        imie = 'Adam'
        nazwisko = 'Małysz'
        wiek = 44
        response = self.create_uczestnik(imie, nazwisko, wiek, client)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class RozgrywkaTests(APITestCase):

    def create_rozgrywka(self, idturniej, id_ucz1, id_ucz2,id_sedzia,wynik_ucz1,wynik_ucz2, client):
        url = reverse(views.UczestnikList.name)
        data = {'idturniej': idturniej,
                'id_ucz1': id_ucz1,
                'id_ucz2': id_ucz2,
                'id_sedzia': id_sedzia,
                'wynik_ucz1': wynik_ucz1,
                'wynik_ucz2': wynik_ucz2
                }
        response = client.post(url, data, format='json')
        return response

    def test_post_and_get_rozgrywka_unauthorized_user(self):
        user = User.objects.create_user('admin', 'admin@ad.com', 'admin1234')
        client = APIClient()
        client.login(username='admin', password='admin1234')
        id_ucz1 = 3
        id_ucz2 = 4
        idturniej = 1
        id_sedzia = 1
        wynik_ucz1 = 1
        wynik_ucz2 = 0
        response = self.create_rozgrywka(idturniej, id_ucz1, id_ucz2, id_sedzia, wynik_ucz1, wynik_ucz2, client)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
