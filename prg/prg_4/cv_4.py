# weight_text = input("Zadej váhu pacienta (kg): ")
# dose_per_kg = 5
#
# try:
#     weight = float(weight_text)
#     dose = weight * dose_per_kg
#     print(f"Dávka: {dose} mg")
# except:
#     print("Chyba: Zadej prosím platné číslo.")
#
######################################################

# number_text = input(f"Zadej váhu pacienta (kg): ")
# number = int(number_text)
#
# try:
#     number = int(number_text)
#     print(number * 2)
# except ValueError:
#     print(f"{number_text} is not a number")
#
######################################################

# Čekáme na správný vstup od uživatele
# Kolikrát se zeptáme? Nevíme - záleží na uživateli!
# age = -1 # Neplatná hodnota pro start
#
# while age < 0 or age > 120:
#     age_str = input("Zadej věk (0-120): ")
#     try:
#         age = int(age_str)
#     except ValueError:
#         print("Zadej prosím celé číslo.")
#         continue
#
# print(f"Věk {age} přijat")

######################################################

# Měříme tepovou frekvenci, dokud není v normě
# heart_rate = measure_sensor()
#
# while heart_rate > 100 or heart_rate < 60:
#     print(f"Abnormální tep: {heart_rate} bpm")
#     alert_nurse()
#     time.sleep(10)
#     heart_rate = measure_sensor()
#
# print("Tep v normě")

######################################################

# counter = 10**10
#
# while counter > 0:
#     print(f"Countdown: {counter}")
#     counter -= 1
# print(f"Start!")

######################################################

# heart_rate = 120
#
# while heart_rate > 60:
#     print(f"Tep: {heart_rate} bpm")
#     heart_rate = heart_rate - 5
#
# print(f"Tep normalizován.")

######################################################

# heart_rate = 70
#
# while True: # Nekonečný cyklus - bezpečný díky break!
#     print(f"Tep: {heart_rate} bpm")
#
#     if heart_rate > 120:
#         print("TACHYKARDIE! Volám lékaře!")
#         break # Kritický stav - ukončíme monitoring
#
#     if heart_rate < 40:
#         print("BRADYKARDIE! Volám lékaře!")
#         break
#
#     # Simulace změny
#     heart_rate_str = input("Nový tep: ")
#     try:
#         heart_rate = int(heart_rate_str)
#     except ValueError:
#         print("Neplatný vstup, zadej celé číslo.")
#         continue
#
# print("Lékař převzal pacienta")

######################################################

numbers = [4, 9, 5, 6, 8, 7, 2, 3]

for number in numbers:
    if number % 3 == 0:
        continue
    while number % 3 != 0:

        if number == 7:
            break
        else:
            print(number)
            break
print(f"Cycle has been ended because of 7 or because of end of list")








