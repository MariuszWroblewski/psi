# 1
# lorem = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym." \
#         "Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki." \
#         "Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym." \
#         "Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum," \
#         "a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach" \
#         "osobistych, jak Aldus PageMaker"
#
# 2
# imie = "Mariusz"
# nazwisko = "Wroblewski"
# liczba_liter1 = lorem.count(nazwisko[2])
# liczba_liter2 = lorem.count(imie[1])
# print("W tekscie jest %i liter %s oraz %i liter %s" % (liczba_liter1, nazwisko[2], liczba_liter2, imie[1]))
#
# 3
# # In file cw1.3
#
# 4
# print(dir(lorem))
# help(lorem.islower)
#
# 5
# print(imie[::-1].title()+" "+nazwisko[::-1].title())
#
# 6
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lista2 = lista[5:]
# lista= lista[0:5]
# print(lista)
# print(lista2)
#
# 7
# lista.extend(lista2)
# lista.insert(0, 0)
# lista_copy = lista.copy()
# lista_copy.sort(reverse=True)
# print(lista_copy)
#
# 8
# k1 = ("Jan Nowak", 133221)
# k2 = ("Anna Maj", 134543)
# k3 = ("Wiktor Dwa", 111222)
# k4 = ("Adam Kopacz", 234432)
# k5 = ("Marcin Ziemia", 567654)
# k6 = ("Aleksandra Jesienna", 112334)
# lista_krotek = k1, k2, k3, k4, k5, k6
# print(lista_krotek)
#
# 9
# slownik = {k1[0]: k1[1], k2[0]: k2[1], k3[0]: k3[1], k4[0]: k4[1], k5[0]: k5[1],
#            k6[0]: k6[1]}
# print(slownik)
# slownik["Adam Małysz"] = {"wiek": 34, "e-mail": "malysz@gmail.com",
# "rok urodzenia": 1990, "adres": "Olsztyn"}
# slownik["Maria Taka"] = {"wiek": 50, "e-mail": "taka@gmail.com",
# "rok urodzenia": 1999, "adres": "Olecko"}
# slownik["Ewelina Kościuszko"] = {"wiek": 51, "e-mail": "kosciuszko@gmail.com",
# "rok urodzenia": 1970, "adres": "Warszawa"}
# print(slownik)
#
# 10
# telefony=[1234556543, 1223221223, 123212321, 111111111, 111111111, 123456789,
#           234567898, 345678909, 786567898, 7656456765, 111111111, 1223221223,
#           1223221223, 123456789, 434343434, 222222222, 222233333, 444444444]
# telefony_zbior=set(telefony)
# print(telefony_zbior)
#
# 11
# for i in range(1, 11):
#     print(i)
#
# 12
# for i in range(100, 19, -5):
#     print(i)
#
# 13