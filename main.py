def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def find_min(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum


def find_max(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


data = [42, 15, 8, 93, 27, 4, 61]

print("Список:", data)
print("Сумма (своя функция):", calculate_sum(data), "| sum():", sum(data))
print("Минимум (своя функция):", find_min(data), "| min():", min(data))
print("Максимум (своя функция):", find_max(data), "| max():", max(data))
