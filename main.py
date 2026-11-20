def calculate_average(measurements):
    total = 0
    for val in measurements:
        total += val
    return total / len(measurements)


def find_minimum(measurements):
    minimum = measurements[0]
    for val in measurements:
        if val < minimum:
            minimum = val
    return minimum


def find_maximum(measurements):
    maximum = measurements[0]
    for val in measurements:
        if val > maximum:
            maximum = val
    return maximum


def count_above_average(measurements):
    avg = calculate_average(measurements)
    count = 0
    for val in measurements:
        if val > avg:
            count += 1
    return count


def find_value(measurements, target):
    for i in range(len(measurements)):
        if measurements[i] == target:
            return i
    return -1


def analyze_measurements(measurements):
    minimum = find_minimum(measurements)
    maximum = find_maximum(measurements)
    average = calculate_average(measurements)
    return minimum, maximum, average


measurements = [12.5, 14.0, 11.8, 15.2, 13.7, 16.1, 14.9, 12.3, 18.0, 11.5]

min_val, max_val, avg_val = analyze_measurements(measurements)
above_avg_count = count_above_average(measurements)

print("Список измерений:", measurements)
print("Количество измерений:", len(measurements))
print("Минимальное значение:", min_val)
print("Максимальное значение:", max_val)
print("Среднее значение:", round(avg_val, 2))
print("Количество значений выше среднего:", above_avg_count)

target = float(input("Введите значение для поиска: "))
index = find_value(measurements, target)

if index != -1:
    print(f"Значение {target} найдено на позиции (индексе): {index}")
else:
    print(f"Значение {target} не найдено в списке")
