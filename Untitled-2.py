import random

# -----------------------------------------------------------------------------------------
# Функция func_data_str - создает/добавляет/перезаписывает/считывает строку базы данных
# Входные параметры:
# filename_dl - название/путь к файлу списка
# in_str_dl - список имён для записи
# del_bl - флаг замены старой строки
# -----------------------------------------------------------------------------------------
# Функция для создания базы данных - строки
def func_data_str(filename_dl: str, in_str_dl: str = "", del_dl: bool = False):
    # Открытие или создание файла если его нет для чтения
    in_str_dl = str(in_str_dl)  
    f_str_dl: str = ""
    # Обработка ошибок
    try:
        if not del_dl:
            with open(filename_dl, "a+") as file_dl:
                file_dl.seek(0)  # Перевод указателя в начало файла
                # Считывание данных из файла с разбиением на строки
                f_str_dl = file_dl.read()
            # Автозакрытие файла

        if del_dl:  # Проверка флага стирания старых имен
            f_str_dl = in_str_dl  # Замена данных в старой строке на новые
        elif in_str_dl:
            # Иначе добавление элементов из новой строки
            f_str_dl = f_str_dl + in_str_dl
        
        if in_str_dl == "" and not del_dl:
            return f_str_dl

        # Открытие или создание файла если его нет для перезаписи
        with open(filename_dl, "w") as file_dl:
            # Запись обновленной строки в файл
            file_dl.write(f_str_dl)  
            # Автозакрытие файла
        # Возврат списка строк из файла
    except PermissionError:
        print("Ошибка доступа к файлу")
        return ("Error")
        
    return f_str_dl
# --End func_data_str

#Функция суммы
def func_sum_list(num_list: list):
    sum1 = sum([x for x in num_list if x % 3 == 0 or str(x)[-1] == '5'])  
        
    return(sum1)

#Данные
number_list: list  = [random.randint(1, 100) for n in range(10)]
#Вывод данных
print("\nМассив случайных чисел от 1 до 100:", number_list)
#Вызов функции суммы
sum_3_5 = func_sum_list(number_list)
#Запись данных в файл
func_data_str("sum_list.txt", sum_3_5, True)
#Вывод данных из файла
print(f"Сумма чисел кратных 3 или оканчивающихся на 5: {func_data_str('sum_list.txt')}")
#Вывод форматированного списка
print(f"Форматированный список: {",".join([str(n) for n in number_list])}\n")


