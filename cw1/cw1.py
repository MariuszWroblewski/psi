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

# d1 = {"Mariusz": 5, "Jan": 3, "Dominik": 4.5, "Maria": 2}
# d2 = {"Polska": "Warszawa", "Rosja": "Moskwa", "Niemcy": "Berlin", "Czechy": "Praga"}
# d3 = {"s": "small", "m": "medium", "l": "large"}
# lista = [d1, d2, d3]
# print(lista[0].f)



#CW2
#1
# listaa = [1, 2, 3, 4, 5, 6]
# listab = [10, 12, 13, 14, 15, 16]


# def f(a_list, b_list):
#     c_list = a_list[0::2] + b_list[1::2]
#     print(c_list)
#
#
# f(listaa, listab)
#
#2
# text = "Tekstowy tekst"
#
#
# def f(data_text):
#     d = {"length: ": len(data_text), "letters: ": list(data_text),
#          "big_letters: ": data_text.upper(), "small_letters: ": data_text.lower()}
#     for key, value in d.items():
#         print(key, ' : ', value)
#
#
# f(text)

#3
# def f(tekst, letter):
#     for i in tekst:
#         a = tekst.replace(letter, "")
#     print(a)
#
#
# f(text, "t")


#4

#5
# class Calculator:
#     def add(self, a, b):
#         print(a+b)
#
#     def difference(self, a, b):
#         print(a-b)
#
#     def multiply(self, a, b):
#         print(a * b)
#
#     def divide(self, a, b):
#         if b != 0:
#             print(a/b)
#         else:
#             print("Nie dziel przez zero")
#
#
# kalkulator = Calculator()
# kalkulator.multiply(3, 4)

#6
# class ScienceCalculator(Calculator):
#     def pow(self, a, b):
#         print(pow(a, b))
#
#
# kalkulator2 = ScienceCalculator()
# kalkulator2.pow(2, 2)


#7
# def f(text):
#     print(text[::-1])
#
# f("koteł")