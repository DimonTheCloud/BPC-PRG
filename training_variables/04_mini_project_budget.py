"""Уровень 4: мини-проект.
Тема: бюджет ученика.
Запусти: python3 04_mini_project_budget.py
"""

print("== Мини-проект: бюджет на учебу ==")

income = float(input("Доход в месяц: "))
course = float(input("Курсы/репетитор: "))
books = float(input("Книги/материалы: "))
other = float(input("Прочие расходы: "))

# TODO 1: посчитай все расходы
total_expenses = course + books + other

# TODO 2: остаток денег
balance = income - total_expenses

# TODO 3: доля расходов на учебу в процентах от дохода
if income > 0:
    study_percent = (total_expenses / income) * 100
else:
    study_percent = 0

print("\n--- Отчёт ---")
print(f"Доход: {income:.2f}")
print(f"Расходы: {total_expenses:.2f}")
print(f"Остаток: {balance:.2f}")
print(f"Учебные расходы: {study_percent:.1f}%")

if balance >= 0:
    print("✅ Бюджет в порядке")
else:
    print("⚠️ Расходы больше дохода — подправь план")

print("✅ Уровень 4 пройден")
