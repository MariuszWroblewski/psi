from django.db import models

# Create your models here.


class Uczestnik(models.Model):
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    nr_tel = models.IntegerField()
    nr_email = models.CharField(max_length=45)
    wiek = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'


class Sedzia(models.Model):
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'


class Turniej(models.Model):
    nazwa = models.CharField(max_length=45)
    miasto = models.CharField(max_length=45)
    ulica = models.CharField(max_length=45, null=True)
    nr_budynku = models.CharField(max_length=45, null=True)
    data = models.DateField(null=True)

    def __str__(self):
        return self.nazwa


class Rozgrywka(models.Model):
    turniej = models.ForeignKey(Turniej, on_delete=models.CASCADE, related_name='mecze')
    ucz1 = models.ForeignKey(Uczestnik, related_name='id1', on_delete=models.CASCADE)
    ucz2 = models.ForeignKey(Uczestnik, related_name='id2', on_delete=models.CASCADE)
    sedzia = models.ForeignKey(Sedzia, on_delete=models.CASCADE)
    wynik_ucz1 = models.IntegerField()
    wynik_ucz2 = models.IntegerField()

    def __str__(self):
        return f'{self.ucz1.imie} {self.ucz1.nazwisko} vs {self.ucz2.imie} {self.ucz2.nazwisko}'
