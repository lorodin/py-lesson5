# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

line = None

file = open('./data/task1/output.txt', 'w')

while True:
    line = input("Input new line (empty line for exit): ")
    if line != '':
        file.write(f'{line}\n')
    else:
        break

file.close()
