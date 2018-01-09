num = int(input("Enter a number: "))

binary = []

while num > 0:

    binary.append(num % 2)

    num //= 2

    
print(''.join(map(str, binary[::-1])))

decimal = 0



for n in range(len(binary)):
    if binary[n] == 1:
        decimal += 2**n
        print(decimal)
print(decimal)
