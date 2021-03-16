"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Подсказка:
Базовый случай здесь - угадали число или закончились попытки
"""


import random


def guessing(num_rand, count=1):
    print('-' * 50)

    if count == 10:
        print('Вы проиграли')
        return num_rand

    num_user = input('Введите число от 1 до 100 для угадывания: ')
    try:
        num_user = int(num_user)
    except ValueError:
        print('Введены некорректные данные!!!')
        guessing(num_rand, count)

    if num_user == num_rand:
        print('Вы выиграли!!!')
        return num_rand
    elif num_user < num_rand:
        print(f'Введеное число МЕНЬШЕ загаданного\n'
              f'Осталось {10 - count} попыток')
    elif num_user > num_rand:
        print(f'Введеное число БОЛЬШЕ загаданного\n'
              f'Осталось {10 - count} попыток')

    return guessing(num_rand, count + 1)


# ---------------------------- main --------------------------
while True:
    print('=' * 20, 'УГАДАЙКА', '=' * 20)
    number = input('Для выхода введите => 0 \n'
                   'Для игры           => любое значение\n'
                   'Введите значение: ')

    if number == '0':
        print('Выход')
        break

    number = random.randint(1, 100)
    print(f'Для контроля {number}')
    print(f'Загаданное число: {guessing(number)}')
