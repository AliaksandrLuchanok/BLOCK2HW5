"""
Дана строка (возможно, пустая), состоящая из букв A-Z:
AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
Нужно написать функцию RLE, которая на выходе даст строку вида:
A4B3C2XYZD4E3F3A6B28И сгенерирует ошибку, если на вход пришла невалидная строка.
Пояснения: Если символ встречается 1 раз, он остается без изменений; Если символ повторяется
более 1 раза, к нему добавляется количество повторений.
"""
def compression():
  use_row = input("Enter your string, please: ")
  use_String = use_row.replace(" ","")
  string_validity = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  temp_validy_str = str(set(use_String).difference(set(string_validity)))
  if  temp_validy_str != "set()":
    return print("Validity error!")
  flag = 0
  string_List = ""
  for i in range(len(use_String)):
    if i < len(use_String)-1:
      if use_String[i] != use_String[i+1]:
        temp = i+1-flag
        if temp > 1:
          string_List += use_String[i] + str(temp)
        else:
          string_List += use_String[i]
        flag = i+1
    elif i+1-flag != 1:
      string_List += use_String[i] + str(i+1-flag)
    else:
      string_List += use_String[i]     
  print(string_List)

compression()
"""
Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит
число А в целую степень B с помощью рекурсии.
*Пример:*
A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8
"""
def exponentiation (number, degree):
  if degree == 1:
    return number
  if degree == 0:
    return 1
  return number*exponentiation (number, degree-1)

use_number = int(input("Enter your number, please: "))
use_degree = int(input("Enter degree of the number, please: "))
print(exponentiation(use_number, use_degree))