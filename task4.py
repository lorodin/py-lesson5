# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

import re

TRANSLATE_DICT = {
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
    "ten": "десять",
}

LINE_PATTERN = r"(" + "|".join(list(TRANSLATE_DICT.keys())) + ") - (\d{1,2})"


def translate(num_str):
    if TRANSLATE_DICT.get(num_str) is None:
        raise ValueError(f"Undefined string number: {num_str}")

    return TRANSLATE_DICT[num_str]


def parse_line(line_num, line):
    try:
        result = re.search(LINE_PATTERN, line.lower()).groups()
        return f"{translate(result[0]).title()} - {int(result[1])}"
    except Exception as err:
        print(f"Error parse file. Wrong value on line: {line_num + 1}.\nError: {err}")
        exit()


def start_app():
    lines = []
    INPUT_FILE = './data/task4/input.txt'
    OUTPUT_FILE = './data/task4/output.txt'

    with open(INPUT_FILE, 'r') as in_file:
        lines.extend([parse_line(line_num, line) for line_num, line in enumerate(in_file.readlines())])

    with open(OUTPUT_FILE, 'w', encoding = 'UTF8') as out_file:
        out_file.write("\n".join(lines))

    print(f"Write file success: {OUTPUT_FILE}")


if __name__ == "__main__":
    start_app()
