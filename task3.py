# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32

import re


def parse_line(line_num, line):
    try:
        result = re.search(r'^(.+)\s(\d+\.?\d*)$', line).groups()
        return {"name": result[0], "salary": float(result[1])}
    except Exception:
        print(f"Error parse file. Wrong value on line: {line_num + 1}")
        exit()


def start_app():
    staffs = []

    with open('./data/task3/input.txt', 'r') as file:
        lines = file.readlines()
        staffs.extend([parse_line(line_num, line) for line_num, line in enumerate(lines)])

    losers = ', '.join([loser['name'] for loser in staffs if loser['salary'] < 20000])
    average = lambda values: sum(values) / len(values) if len(values) != 0 else 0

    print(f"Losers (salary < 20000): {losers}")
    print(f"         Average salary: {average([staff['salary'] for staff in staffs])}")


if __name__ == "__main__":
    start_app()
