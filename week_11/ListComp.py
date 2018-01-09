
fahr_celsius = [(x, int((x - 32) * 5 / 9)) for x in range(0, 101, 10)]

print("Fahr \t Cels")
for f, c in fahr_celsius:
    print("{0:<3} \t {1:<3}".format(f, c))
print("\n")
count = 0
while count <= 5:
    print(str(count) + ',')
    count += 1
