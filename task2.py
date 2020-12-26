# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

file = open('./data/task2/input.txt', 'r')

lines = [line.replace('\n', '') for line in file]

print(f"Lines count: {len(lines)}")

for line_num, line in enumerate(lines, start = 1):
    print(f"Line[{ line_num }] length: { len(line) }")

