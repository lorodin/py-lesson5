# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


import re


def parse_line(line_num, line):
    try:
        parse = re.match(r'^(.+):\s(.*)', line).groups()
        hours = re.findall(r'(\d+)\((л|пр|лаб)\)', parse[1])
        return parse[0], sum([int(h[0]) for h in hours])
    except Exception as err:
        print(f"Error parse line: {line_num}.\nError: {err}")


def start_app():
    with open('./data/task6/input.txt', 'r', encoding = "UTF8") as file:
        result = {
            value[0]: value[1]
            for value in [
                parse_line(line_num, line)
                for line_num, line in enumerate(file)
            ]}
    print(f"Result: {result}")


if __name__ == "__main__":
    start_app()
