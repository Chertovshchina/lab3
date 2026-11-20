numbers = [42, 15, 8, 93, 27, 4, 61, 19, 75, 30]

print("Исходный список:", numbers)
print("Количество элементов:", len(numbers))
print("Сумма элементов:", sum(numbers))
print("Минимальное значение:", min(numbers))
print("Максимальное значение:", max(numbers))
print("Среднее арифметическое:", sum(numbers) / len(numbers))

sorted_copy = sorted(numbers)
print("Отсортированная копия sorted():", sorted_copy)
print("Исходный список после sorted():", numbers)

numbers.sort()
print("Исходный список после метода sort():", numbers)
