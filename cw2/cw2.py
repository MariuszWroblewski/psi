import file_manager
#1
# listaa = [1, 2, 3, 4, 5, 6]
# listab = [10, 12, 13, 14, 15, 16]
#
#
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
#
#3
# def f(tekst, letter):
#     for i in tekst:
#         a = tekst.replace(letter, "")
#     print(a)
#
#
# f(text, "t")


#4
# def f(temp, temp_type):
#     if(temp_type=='celsjusz'):
#         print("Stopnie Fahrenheit'a: " + str(1.8 * temp+32))
#         print("Stopnie Kelwina: " + str(temp + 273.15))
#         print("Stopnie Rankine: " + str(temp + 273.15))
#     elif(temp_type=='fahrenheit'):
#         print("Stopnie Celsjusza: " + str((temp - 32)/1.8))
#         print("Stopnie Kelwina: " + str((temp + 459.67) * (5/9)))
#         print("Stopnie Rankine: " + str(temp + 459.67))
#     elif(temp_type=='rankine'):
#         print("Stopnie Celsjusza: " + str((temp / 1.8) - 273.15))
#         print("Stopnie Kelwina: " + str((temp + 459.67) * (5 / 9)))
#         print("Stopnie Fahrenheit'a: " + str(temp - 459.67))
#
#
# f(12, 'rankine')
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
#9
# print("File before update: ")
# fil = file_manager.FileManager('test.txt')
# fil.read_file()
# print("File after update:")
# fil.update_file(' second simple text ')
# fil.read_file()
