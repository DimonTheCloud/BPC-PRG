# fahrenheit = int(input("Temperature: "))
# celsius = (fahrenheit - 32) * 5/9
# print(f"Fahrenheit: {fahrenheit}°F, Celsius: {celsius:.2f}°C")

#############################################

# heslo = input("Password: ")
# password_length = (len(heslo))
# if len(heslo) < 8:
#     print("Heslo je příliš krátké!")
# else:
#     print(f"Tvoje heslo má {password_length} znaků ")

#############################################

# hospital_name = "Nemocnice u Sv. Anny"
# part = "Ambulatorni oddeleni"
#
# print("=" * (len(hospital_name + part) + 3))
# print(f"{hospital_name} - {part}")
# print("=" * (len(hospital_name + part) + 3))

#############################################

# # Vytvoř program pro výpočet BMI s pěkným výstupem
# name = input("Jméno: ")
# weight = float(input("Váha (kg): "))
# height = float(input("Výška (m): "))
#
# bmi = weight / (height ** 2)
#
# print(f"Pacient: {name.title()}")
# print(f"Váha: {weight:.1f} kg")
# print(f"Výška: {height:.2f} m")
# print(f"BMI: {bmi:.2f}")
#
# # Vyhodnocení
# if bmi < 18.5:
#     category = "podváha"
# elif bmi < 25:
#     category = "normální váha"
# elif bmi < 30:
#     category = "nadváha"
# else:
#     category = "obezita"
#
# print(f"Kategorie: {category}")

#############################################

# systolic = int(input("Systolic pressure: "))
# diastolic = int(input("Diastolic pressure: "))
#
# MAP = (systolic + 2 * diastolic) / 3
#
# print(f"MAP: {MAP:.1f}mmHg")



# RC = "9501152345"
# DD = RC[4:6]
# MM = RC[2:4]
# RR = RC[0:2]
# print(f"Datum narození: {DD}.{MM}.{RR}")

#############################################

# DNA = "ACGTTAGCTA"
# count = 0
# for char in DNA:
#     if char == "C" or char == "G":
#         count += 1
#     else:
#         continue
#
# print(f"GC obsah: {count} znaků")

#############################################

# name = "         KovaLski RiKoveC  "
#
# name_formatted = name.strip().lower()
# print(f"Normální formát: {name_formatted}")

#############################################

# cities = ["Praha", "Brno", "Ostrava", "Plzeň"]
#
# # Bez enumerate - ruční čítání:
# index = 0
# for city in cities:
#     print(f"{index + 1}. {city}")
#     index += 1
#
# # S enumerate - elegantnější:
# for i, city in enumerate(cities, start=1):
#     print(f"{i}. {city}")

#############################################

# diagnoza = "Diabetes;Hypertenze;Astma;Migrena"
# list_diagnoza = diagnoza.split(";")
#
# for num, diagnoza in enumerate(list_diagnoza, start=1):
#     print(f"{num}. {diagnoza}")

#############################################

# admin_name = "dimon_the_cloud"
#
# admin_name = input("Please enter your name: ").strip().lower().replace(" ", "_")
# if admin_name == "dimon_the_cloud":
#     print("Přihlášení úspěšné!. Welcome, dimon_the_cloud")
# else:
#     print("Neznámý uživatel!")

#############################################

# text = "Python is great!"
# vowel_count = 0
# consonant_count = 0
#
# for char in text:
#     if char.isalpha():  # Pouze písmena
#         if char.lower() in "aeiou":
#             vowel_count += 1
#         else:
#             consonant_count += 1
#
# print(f"Samohlásky: {vowel_count}")
# print(f"Souhlásky: {consonant_count}")

#############################################

# sentence = "I love Python!"
# if "python" in sentence.lower():
#     print("Obsahuje python")

#############################################

# RC = input("RC: ")
#
# DD = RC[4:6]
# MM = RC[2:4]
# RR = RC[0:2]
# pohlavi = int(MM) - 50
# if len(RC) == 10 and RC.isdigit() == True:
#     print(f"=== ANALÝZA RODNÉHO ČÍSLA ===")
#     print(f"Rodné číslo: {RC}")
#     print(f"Platnost: VALIDNÍ")
#     print(f"Datum narození: {DD}.{MM}.{RR}")
#     if pohlavi > 50:
#         print(f"Pohlavi: žena")
#     else:
#         print(f"Pohlavi: muž")
#     print(f"Kontrolní součet: PLATNÝ")
# else:
#     print(f"Zadane RC neni platne!")

#############################################

data = """  JAN NOVÁK  ,  9501152345,  DIABETES  
  MARIE   SVOBODOVÁ,9652253456,HYPERTENZE
PETR Dvořák,8803154567,  Astma  """

data_formatted = data.split("\n",",")
print(data_formatted)









