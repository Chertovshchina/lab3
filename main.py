measurements = (12.5, 14.0, 11.8, 15.2, 13.7, 16.1, 14.9, 12.3)

first, second = measurements[0], measurements[1]
print("Первое значение:", first)
print("Второе значение:", second)

temp_list = list(measurements)
temp_list[0] = 99.9
measurements = tuple(temp_list)

print("Обновлённый кортеж:", measurements)
