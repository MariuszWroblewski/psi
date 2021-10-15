#1
lorem = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym." \
        "Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki." \
        "Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym." \
        "Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum," \
        "a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach" \
        "osobistych, jak Aldus PageMaker"


#2
imie = "Mariusz"
nazwisko = "Wroblewski"
# liczba_liter1 = lorem.count(nazwisko[2])
# liczba_liter2 = lorem.count(imie[1])
# print("W tekscie jest %i liter %s oraz %i liter %s" % (liczba_liter1, nazwisko[2], liczba_liter2, imie[1]))

#3

#4
# print(dir(lorem))
# help(lorem.islower)

#5
print(nazwisko[::-1].title()+" "+imie[::-1].title())

#6
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = lista[5:]
lista= lista[0:5]
print(lista)
print(lista2)


