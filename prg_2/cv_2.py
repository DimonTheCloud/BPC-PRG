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

DNA = "ACGTTAGCTA"
count = 0
for char in DNA:
    if char == "C" or char == "G":
        count += 1
    else:
        continue

print(f"GC obsah: {count} znaků")











































