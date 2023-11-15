import datetime
import os
import random
from datetime import datetime


def create_file_with_random_numbers(file_path, size_in_mb):
    """ Створює файл із випадковими числами заданого розміру """
    size_in_bytes = size_in_mb * 1024 * 1024 * 1024  # перетворення розміру з MB в B
    current_size = 0

    with open(file_path, 'w') as file:
        while current_size < size_in_bytes:
            for i in range(1, 9):
                num = random.randint(0, 1000000)
                file.write(f"{num} ")
                current_size += len(str(num)) + 1  # +1 для урахування символа нового рядка
            file.write(f"{num}\n")
            current_size += len(str(num)) + 1  # +1 для урахування символа нового рядка

    print(f"Файл '{file_path}' створено з розміром приблизно {size_in_mb} GB.")


# Використання функції
create_file_with_random_numbers('1GB.txt', 1)  # Створює файл розміром 1GB
print("file created")


def merge_series(file1, file2, output_file):
    """ Зливає дві серії у вихідний файл """
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
        num1 = f1.readline()
        num2 = f2.readline()
        while num1 and num2:
            if int(num1) < int(num2):
                out.write(num1)
                num1 = f1.readline()
            else:
                out.write(num2)
                num2 = f2.readline()
        while num1:
            out.write(num1)
            num1 = f1.readline()
        while num2:
            out.write(num2)
            num2 = f2.readline()


def split_to_series(input_file, temp_file1, temp_file2):
    """ Розділяє вхідний файл на серії та записує їх у два тимчасових файлів """
    with open(input_file, 'r') as inp, open(temp_file1, 'w') as out1, open(temp_file2, 'w') as out2:
        current_out = out1
        previous_num = None
        for num in inp:
            if previous_num is not None and int(num) < int(previous_num):
                current_out = out2 if current_out is out1 else out1
            current_out.write(num)
            previous_num = num


def direct_merge_sort(input_file):
    """ Основна функція для прямого злиття """
    temp_file1 = 'temp1.txt'
    temp_file2 = 'temp2.txt'
    series_size = 512 * 1024 * 1024
    file_size = os.path.getsize(input_file)

    while series_size < file_size:
        split_to_series(input_file, temp_file1, temp_file2)
        merge_series(temp_file1, temp_file2, input_file)
        series_size *= 2

    os.remove(temp_file1)
    os.remove(temp_file2)

current_time = datetime.now()
# Виклик функції сортування
direct_merge_sort('1GB.txt')
print("file sorted")
next_time = datetime.now()
print(f"Time taken: {next_time - current_time}")
