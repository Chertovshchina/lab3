def find_element(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1


data = [10, 20, 30, 40, 50, 60, 70]

print("Список:", data)
print("Индекс элемента 40:", find_element(data, 40))
print("Индекс элемента 99:", find_element(data, 99))
