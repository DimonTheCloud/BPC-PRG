# def greet_patient():
#     name = input("Please enter your name: ")
#     print(f"Ahoj, {name}")
#
#     return greet_patient()
#
# print(greet_patient())

#####################################################

# def has_fever():
#     actual_temp = input("Please enter your temperature: ")
#     if int(actual_temp) >= 39:
#         return print("You have fever!")
#     else:
#         return print("Your temperature is good")
#
# result = has_fever()

#####################################################

# temp_c = input("Enter temperature in Celsius: ")
#
# def celsius_to_fahrenheit():
#     temp_f = float(temp_c) * 9 / 5 + 32
#     return temp_f
#
# result = celsius_to_fahrenheit()
# print(f"{result:.1f} °F")

#####################################################

# # Seznam měření systolického tlaku za týden
# blood_pressure = [120, 125, 118, 130, 135, 128, 122]
#
# max_pressure = max(blood_pressure)
# min_pressure = min(blood_pressure)
# print(max(blood_pressure))
# print(min(blood_pressure))
#
# count = 0
# for pressure in blood_pressure:
#     if pressure > 130:
#         count += 1
#     else:
#         continue
#
# days = ["Po", "Út", "St", "Čt", "Pá", "So", "Ne"]
# result = list(zip(days, blood_pressure))
# print(result)

#######################################################

# patients = []
#
# patients.append("Jan Novák")
# patients.append("Marie Svobodová")
# patients.append("Petr Dvořák")
# patients.append("Anna Černá")
# patients.append("Tomáš Novotný")
# print(f"Původní seznam: {patients}")
#
# patients.pop(0)
# print(f"Po ošetření: {patients}")
#
# patients.remove("Petr Dvořák")
# print(f"Po zrušení: {patients}")
#
# patients.insert(0, "Karel Urgentní")
# print(f"Po urgenci: {patients}")
#
# patients.sort()
# print(f"Seřazeno:{patients}")

#######################################################

# # Data: [jméno, teplota_den1, teplota_den2, teplota_den3]
# temperature_log = [
#         ["Jan Novák", 36.5, 36.7, 36.6],
#         ["Marie Svobodová", 37.2, 38.1, 38.5],
#         ["Petr Dvořák", 36.8, 36.9, 37.0]
# ]
#
# for patient in temperature_log:
#     name = patient[0]
#     temps = patient[1:]
#
#     average = sum(temps) / len(temps)
#     maximum = max(temps)
#
#     print(f"Jméno pacienta: {name}")
#     print(f"Průměr: {average:.1f}°C")
#     print(f"Maximum: {maximum:.1f}°C")
#
#     if maximum >= 38.0:
#         print("POZOR: Byla zaznamenána horečka!")
#
#     print()
#

#######################################################
#
# measurements = [
#     ["Jan", 118, 78],
#     ["Marie", 135, 88],
#     ["Petr", 125, 82],
#     ["Anna", 145, 95],
#     ["Tomáš", 119, 79],
#     ["Eva", 142, 91]
# ]
# systolic = measurements[1][1]
# diastolic = measurements[1][2]
#
# def classify_pressure(systolic, diastolic):
















#######################################################

# def analyze_dna():
#     DNA_seq = input(f"Add your DNA sequence: ")
#     amount_A = DNA_seq.count("A")
#     amount_T = DNA_seq.count("T")
#     amount_G = DNA_seq.count("G")
#     amount_C = DNA_seq.count("C")
#     percent_GC = (amount_G + amount_C) / len(DNA_seq) * 100
#
#     return print(list([amount_A, amount_T, amount_G, amount_C, percent_GC]))
# result = analyze_dna()

#######################################################

# DNA_seq = input(f"Add your DNA sequence: ")
# DNA_motif = input(f"Add your DNA motifs: ")
#
# def find_motifs(DNA_seq, DNA_motif):
#     positions = find_motifs(DNA_seq, DNA_motif)
#     return print(positions)
#
#
# result = find_motifs()

#######################################################















