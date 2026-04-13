"""Уровень 1: базовые переменные.
Запусти: python3 01_variables_basics.py
"""

# TODO 1: создай переменную student_name со своим именем
student_name = "Твоё имя"

# TODO 2: создай переменную study_hours (сколько часов в неделю учишься)
study_hours = 0

# TODO 3: создай переменную is_motivated (True/False)
is_motivated = True

print("Привет,", student_name)
print("Часов в неделю:", study_hours)
print("Есть мотивация:", is_motivated)

# Проверка-пазл
if isinstance(student_name, str) and isinstance(study_hours, int) and isinstance(is_motivated, bool):
    print("✅ Уровень 1 пройден")
else:
    print("❌ Проверь типы переменных")
