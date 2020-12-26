# 7. Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджер контекста.

import json


def parse_line(line_num, line):
    result = line.split(' ')
    if len(result) < 4:
        print(f'Error parse line {line_num}. Must be 4 arguments')
        exit()
    try:
        return result[0], float(result[2]) - float(result[3])
    except Exception as err:
        print(f"Error parse line {line_num}.\nError: {err}")
        exit()


def profits_companies(companies):
    for company in companies:
        if company[1] > 0:
            yield company[1]


def start_app():
    average = lambda data: sum(data) / len(data) if len(data) != 0 else 0

    with open('./data/task7/input.txt', 'r', encoding = 'UTF8') as file:
        companies = [parse_line(line_num, line) for line_num, line in enumerate(file)]
        result = [
            {company[0]: company[1] for company in companies},
            {'average_profit': average(list(profits_companies(companies)))}]

    with open('./data/task7/output.json', 'w', encoding = 'UTF8') as file:
        file.write(json.dumps(result))

    print("Write json success: ./data/task7/output.json")


if __name__ == "__main__":
    start_app()
