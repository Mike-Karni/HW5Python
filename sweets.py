'''1. Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?'''

import random

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x

def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

name1 = input("Введите имя первого игрока ")
name2 = input("Введите имя второго игрока ")
sweetsQauntity = int(input("Введите количество конфет на столе "))

randomChoice = random.randint(0,2)
if randomChoice == 0:
    print("Первым ходит игрок 1 ")
else:
    print("Первым ходит игрок 2 ")

counter1 = 0
counter2 = 0

while sweetsQauntity>28:
    if randomChoice==0:
        k = input_dat(name1)
        counter1 += k
        sweetsQauntity -= k
        flag = False
        p_print(name1, k, counter1, sweetsQauntity)

    else:
        k = input_dat(name2)
        counter2 += k
        sweetsQauntity -= k
        flag = True
        p_print(name2, k, counter2, sweetsQauntity)

if randomChoice==0:
    print(f"Выиграл {name1}")
else:
    print(f"Выиграл {name2}")