"""Уровень 2: типы и ввод данных.
Запусти: python3 02_types_and_input.py
"""

print("== Анкета ученика ==")

# TODO 1: спроси возраст через input и сохрани в переменную age
age = int(input("Сколько тебе лет? "))

# TODO 2: спроси средний балл и сохрани как float в gpa
gpa = float(input("Твой средний балл? "))

# TODO 3: спроси любимый предмет и сохрани в subject
subject = input("Любимый предмет: ")

adult = age >= 18

print("\nРезультат:")
print(f"Возраст: {age} ({type(age).__name__})")
print(f"Средний балл: {gpa} ({type(gpa).__name__})")
print(f"Предмет: {subject} ({type(subject).__name__})")
print(f"Совершеннолетний: {adult} ({type(adult).__name__})")

if isinstance(age, int) and isinstance(gpa, float) and isinstance(subject, str):
    print("✅ Уровень 2 пройден")
else:
    print("❌ Проверь преобразование типов")
