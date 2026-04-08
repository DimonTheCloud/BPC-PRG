# def main():
#     print("Hello from cviceni")
#
#     if __name__ == "__main__":
#         main()

###########################################


# name = "Dmytro"
# age = 20
# greeting = "Hello"
# print(greeting)
# print(name)
# print(f"Vek:{age}")
###########################################

# course =  "Algoritmizace"
# print(f"Vitejte v kurzu {course}")

###########################################

# monthly_income = 25000
# MONTHS = 12
# TAX_RATE_PCT = 0.15
#
# year_income = monthly_income * MONTHS
# year_tax = year_income * TAX_RATE_PCT
#
# print(f"Year income: {year_income}")
# print(f"Year tax: {year_tax}")

###########################################

# heart_rate = 105 or 95
# TACHYCARDIA_LIMIT = 100
#
# if heart_rate > TACHYCARDIA_LIMIT:
#     print(f"Zrychleny tep: {heart_rate}")
# else:
#     print("Srdecni frekvence v norme")

###########################################

# number = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
# for i in range(10):
#     print(f"Bed No.{i}")
#

###########################################


# temperatures = [36.6, 37.2, 38.1, 36.9, 37.5]
# for temperature in temperatures:
#     print(f"Teplota: {temperature}°C")

###########################################

# heart_rate = 72
# if heart_rate > 100:
#     print("Tachykardie!")

###########################################

# patient_name = "Jan Novák"
# print(f"Pacient: {patient_name}")

###########################################

# temperature = 37.5
# if temperature > 38.0:
#     print("Horečka!")

###########################################

# temperatures = [36.6, 37.2, 38.1]
# first_temp = temperatures[0]
# last_temp = temperatures[2]
# print(last_temp)

###########################################

# temperature = 39
# heart_rate = 105

# if temperature >= 39.0 or heart_rate >= 110.0:
#     print("VAROVÁNÍ: Zavolejte lékaře!")
# else:
#     print("Vitální funkce v pořádku")

###########################################

# Seznam teplot
# temperatures = [36.6, 38.5, 37.2, 39.1, 36.9, 38.2]

# Počítadlo pacientů s horečkou
# fever_count = 0
#
# for temp in temperatures:
#     if temp >= 38.0:
#         fever_count += 1  # Zkrácený zápis pro: fever_count = fever_count + 1
#
# print(f"Celkem pacientů: {len(temperatures)}")
# print(f"Pacientů s horečkou: {fever_count}")

###########################################

# glucose_levels = [4.5, 6.2, 3.8, 5.1, 7.5, 4.9]
#
# for glucose_level in glucose_levels:
#     if glucose_level > 5.6:
#         print(f"Hypoglykémie: {glucose_level} mmol/l")
#     elif glucose_level < 3.9:
#         print(f"Hypoglykémie: {glucose_level} mmol/l")
#     else:
#         print(f"V normě: {glucose_level} mmol/l")


###########################################


# temperatures = [36.6, 38.5, 37.2, 39.1, 36.9, 38.2, 37.5, 40.1]
# FEVER_LIMIT = 38.0
# HIGH_FEVER_LIMIT = 39.5
# normal_count = 0
# fever_count = 0
# high_fever_count = 0
#
# for temp in temperatures:
#     if temp > HIGH_FEVER_LIMIT:
#         high_fever_count += 1
#     elif temp >= FEVER_LIMIT and temp < HIGH_FEVER_LIMIT:
#         fever_count += 1
#     else:
#         normal_count += 1
#
# print(f"=== ANALÝZA TEPLOT === ")
# print(f"Celkem měření: {len(temperatures)}")
# print("Normální teplota: {normal_count}")
# print(f"Horečka: {fever_count}")
# print(f"Vysoká horečka: {high_fever_count}")


###########################################

# weights = [75, 68, 92, 58, 80]
# heights = [1.80, 1.65, 1.90, 1.60, 1.75]
#
# overweight_count = 0
#
# for i in range(5):
#     bmi = weights[i] / (heights[i] ** 2)
#     if bmi >= 25:
#         overweight_count += 1
#     else:
#         overweight_count += 0
#
# print(f"Patient with overweight is {overweight_count}")


###########################################

# systolic = [120, 140, 135, 110, 155, 125, 145]
# diastolic = [80, 90, 85, 70, 95, 82, 92]
#
# NORMAL_SYS_LIMIT = 130
# NORMAL_DIA_LIMIT = 85
#
# normal_count = 0
# high_count = 0
#
# for i in range(len(systolic)):
#     # print(f"Patient {i}")
#
#     if systolic[i] > NORMAL_SYS_LIMIT or diastolic[i] > NORMAL_DIA_LIMIT:
#         high_count += 1
#
#
#         # print(f"Pacient n.{i}: {systolic[i]}/{diastolic[i]} mmHg")
#
#     elif systolic[i] < NORMAL_SYS_LIMIT or diastolic[i] < NORMAL_DIA_LIMIT:
#         normal_count += 1
#
#
# print(f"Zvýšený tlak: {high_count}")
# print(f"Normalni tlak: {normal_count} pacient")

###########################################


# heart_rates = [72, 85, 68, 105, 78, 92, 70, 88]
#
# total = 0
# min_rate = heart_rates[0]
# max_rate = heart_rates[0]
#
# for heart_rate in heart_rates:
#     total += heart_rate
#     if total < min_rate:
#         min_rate = heart_rate
#     elif total > max_rate:
#         max_rate = heart_rate
#
#
# avg = total / len(heart_rates)
#
# print(f"=== ANALÝZA SRDEČNÍ FREKVENCE ===")
# print(f"Počet měření: {len(heart_rates)}")
# print(f"Average value: {avg:.1f} bpm")
# print(f"Min value: {min_rate} bpm")
# print(f"Max value: {max_rate} bpm")


###########################################


# if password := "heslo123":
#     print("Přístup povolen"),
# else:
#     print(Přístup odepřen)

###########################################

# n = 3
# for n in range(n+1):
#     print(n)

###########################################

# count = 3
#
# for i in range(count):
#     print(f"Ahoj")

###########################################

# n = 4
#
# for i in range(n):
#     if i % 2 == 0:
#         print(f"{i} je sudé")
#     else:
#         print(f"{i} je liché")

###########################################

# words = ["pes", "kočka", "slon", "žirafa"]
#
# long_w = 0
#
# for word in words:
#     if len(word) >= 5:
#         long_w = long_w + 1
#
# print(f"Počet dlouhých slov: {long_w}")

###########################################

# product = 1
# numbers = [2, 3, 4]
#
# for number in numbers:
#     product = product * number
#
# print(f"product = {product}")

###########################################

# sum_odd = 0
# numbers = [1, 2, 3, 4, 5]
#
# for number in numbers:
#     if number % 2 != 0:
#         sum_odd = sum_odd + number
#     else:
#         continue
# print(sum_odd)
###########################################

# numbers = [8, 3, 12, 5, 9]
# value = numbers[0]
# for number in numbers:
#     if number < value:
#         value = number
#
# print(value)



