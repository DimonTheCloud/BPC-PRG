#надо сделать так, что бы вывелись все парные числа и в конце написать сколько их было в общем.
count = 0
for n in range(1, 10):
    if n % 2 == 0:
        print(n)
        count += 1
    else:
        continue
print(f"Amount of even numbers: {count}")
