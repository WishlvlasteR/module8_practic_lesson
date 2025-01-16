def personal_sum(numbers):
    incorrect_data = 0
    result = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
            print(f'Сумма чисел {result}. Кол-во некорректных данных {incorrect_data}')
    return result, incorrect_data


def calculate_average(numbers):
    try:
        total_sum, incorrect_count = personal_sum(numbers)
        count = len(numbers) - incorrect_count
        return total_sum / count
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
