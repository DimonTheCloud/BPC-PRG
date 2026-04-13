"""Уровень 3: операции и формулы.
Запусти: python3 03_operations_and_formulas.py
"""

# Дано:
lessons_per_week = 5
minutes_per_lesson = 45
weeks = 4

# TODO 1: посчитай общее количество минут за месяц
total_minutes = lessons_per_week * minutes_per_lesson * weeks

# TODO 2: переведи минуты в часы (float)
total_hours = total_minutes / 60

# TODO 3: если цель 20 часов в месяц, посчитай сколько не хватает или + если перевыполнил
goal_hours = 20
delta = total_hours - goal_hours

print("Минут за месяц:", total_minutes)
print("Часов за месяц:", round(total_hours, 2))
print("Разница с целью:", round(delta, 2))

if total_minutes > 0 and isinstance(total_hours, float):
    print("✅ Уровень 3 пройден")
else:
    print("❌ Проверь вычисления")
