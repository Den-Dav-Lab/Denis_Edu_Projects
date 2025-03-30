# Импортируем библиотеку numpy с псевдонимом np
import numpy as np
simple_list = [1, 2, 3, 4, 5] # Создаем простой пример списка языка Python
# Конвертируем созданный список в массив Numpy
my_first_ndarray = np.array(simple_list, dtype=int)
print(type(my_first_ndarray)) # Тип созданного объекта
print("Элементы массива", my_first_ndarray) # Результат стандартного вывода
# Создание массивов и вывод типа данных 
my_first_ndarray2 = np.array([1, 2, 3])
print("Числа [1, 2, 3]", my_first_ndarray2.dtype.type)
my_first_ndarray2 = np.array(['1', '2', '3'])
print("Строки ['1', '2', '3']", my_first_ndarray2.dtype.type)
my_first_ndarray2 = np.array(['1', 2, 3])
print("Смешанные ['1', 2, 3]", my_first_ndarray2.dtype.type)

