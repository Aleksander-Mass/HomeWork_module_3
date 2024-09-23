def calculate_structure_sum(data):
    total_sum = 0

    # Проверяем каждый элемент структуры
    if isinstance(data, int):  # Если это число, добавляем его
        total_sum += data
    elif isinstance(data, str):  # Если это строка, добавляем её длину
        total_sum += len(data)
    elif isinstance(data,
                    (list, tuple, set)):  # Если это список, кортеж или множество, рекурсивно обрабатываем их элементы
        for item in data:
            total_sum += calculate_structure_sum(item)
    elif isinstance(data, dict):  # Если это словарь, обрабатываем и ключи, и значения
        for key, value in data.items():
            total_sum += calculate_structure_sum(key)
            total_sum += calculate_structure_sum(value)

    return total_sum

# Пример использования функции
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result) # => 99
