# Seznam měření systolického tlaku za týden
blood_pressure = [120, 125, 118, 130, 135, 128, 122]

max_pressure = max(blood_pressure)
min_pressure = min(blood_pressure)
print(max(blood_pressure))
print(min(blood_pressure))

count = 0
for pressure in blood_pressure:
    if pressure > 130:
        count += 1
    else:
        continue

days = ["Po", "Út", "St", "Čt", "Pá", "So", "Ne"]
result = list(zip(days, blood_pressure))
print(result)

