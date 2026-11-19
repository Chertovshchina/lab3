def greet(name):
    print("Привет,", name)


def square(number):
    return number ** 2


def max_of_two(a, b):
    if a > b:
        return a
    return b


greet("Николай")
greet("Анна")

print(square(4))
print(square(7))

print(max_of_two(10, 25))
print(max_of_two(42, 18))
