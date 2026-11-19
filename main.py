numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("Первый элемент:", numbers[0])
print("Третий элемент:", numbers[2])
print("Последний элемент:", numbers[-1])

numbers[1] = 25
numbers.append(110)
numbers.remove(50)

print("Итоговый список:", numbers)
print("Количество элементов:", len(numbers))
