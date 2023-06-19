# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.


num_rows = int(input("количество строк: "))
num_columns = int(input("количество столбцов: "))
operation = lambda a, b: a * b

create_operation_table = lambda operation, a, b: [[operation(x, y) for x in range(1, a+1)] for y in range(1, b+1)]

def print_operation_table(matrix, num_rows, num_columns):
    for i in range(num_rows):
        for j in range(num_columns):
            print(matrix[j][i], end ="\t")
        print(end = "\n")
    
print_operation_table(create_operation_table(operation, num_rows, num_columns), num_rows, num_columns)