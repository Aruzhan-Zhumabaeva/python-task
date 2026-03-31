# 1
n = int(input())
print("Четное" if n % 2 == 0 else "Нечетное")

# 2
name = input()
print(f"Привет, {name}!")

# 3
n = int(input())
print(f"Квадрат числа {n} равен {n**2}")

# 4
age = int(input())
print("Доступ разрешен" if age >= 18 else "Маловат еще")

# 5
word = input()
n = int(input())
for i in range(n):
    print(word, end=" ")
print()

# 6
a, b = map(int, input().split())
print(max(a, b))

# 7
n = int(input())
if n > 0:
    print("Плюс")
elif n < 0:
    print("Минус")
else:
    print("Ноль")

# 8
s = input()
print("Верно" if s == "python123" else "Ошибка")

# 9
i = 1
while i <= 5:
    print(i, end=" ")
    i += 1
print()

# 10
a, b = map(int, input().split())
print(f"Сумма {a} и {b} равна {a + b}")

# 11
n = int(input())
print("В диапазоне" if 10 <= n <= 20 else "Не в диапазоне")

# 12
word = input()
print("Длинное" if len(word) > 5 else "Короткое")

# 13
n = int(input())
while n < 100:
    n *= 2
print(n)

# 14
n = int(input())
if not n:
    print("Это ноль")

# 15
for i in range(1, 11):
    print(2 * i, end=" ")
print()

# 16
price = float(input())
print(price * 0.9 if price > 1000 else price)

# 17
grade = int(input())
if grade == 5:
    print("Отлично")
elif grade == 4:
    print("Хорошо")
else:
    print("Старайся")

# 18
for i in range(5, 0, -1):
    print(i, end=" ")
print()

# 19
day = input()
print("Выходной" if day in ["суббота", "воскресенье"] else "Работа")

# 20
n = int(input())
print("Да" if n % 3 == 0 else "Нет")

# 21
n = int(input())
total = 0
for i in range(1, n + 1):
    total += i
print(total)

# 22
for i in range(2, 11, 2):
    print(i, end=" ")
print()

# 23
word = input()
print("Найдена" if "а" in word else "Нет")

# 24
while True:
    s = input("Введите слово (или стоп): ")
    if s == "стоп":
        print("Выход из программы")
        break

# 25
n = int(input())
print(f"Результат: {n * 10}")

# 26
s = input()
print("Пусто" if s == "" else "Текст есть")

# 27
a, b = map(int, input().split())
if a > 0 and b > 0:
    print(a * b)

# 28
n = int(input())
while n >= 0:
    print(n, end=" ")
    n -= 1
print()

# 29
a, b = map(int, input().split())
print((a + b) / 2)

# 30
login = input()
if login != "admin":
    print("Доступ запрещен")

# 31
for i in range(1, 5):
    print(i**2, end=" ")
print()

# 32
t = int(input())
if t < 0:
    print("Мороз")
elif t > 25:
    print("Жара")
else:
    print("Нормально")

# 33
s = input()
print(f"{s}{s}")

# 34
a, b, c = map(int, input().split())
if 7 in [a, b, c]:
    print("Все ок")

# 35
n = int(input())
if n % 2 == 0 and n % 5 == 0:
    print("Подходит")

# 36
word = input()
print(f"Первая буква: {word[0]}")

# 37
word = input()
if word.startswith("а"):
    print("Начинается на А")

# 38
n = int(input())
print("Счастливое число!" if n == 7 else "Обычное число")

# 39
a, b = map(int, input().split())
print(abs(a - b))

# 40
name, job = input().split()
print(f"{name} — это отличный {job}!")