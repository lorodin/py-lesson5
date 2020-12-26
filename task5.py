# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint


def start_app():
    rnd_list = [str(randint(0, 100)) for i in range(randint(10, 20))]
    with open("./data/task5/output.txt", "w") as file:
        file.write(' '.join(rnd_list))
    with open("./data/task5/output.txt", "r") as file:
        content = file.read()
        print(f"File content: {content}")
        print(f"Numbers sum: {sum([int(n) for n in content.split(' ')])}")


if __name__ == "__main__":
    start_app()
