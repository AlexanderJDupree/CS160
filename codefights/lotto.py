from random import randint

lottoMatrix = []
# Asks for numbers to be scrambled, converts it to a list
series = int(input("How many series of numbers to be inputed? "))
for n in range(series):
    lottoNumbers = input('Enter your lottery numbers for row %r: ' % n)
    lotto_numbers = list(map(int, lottoNumbers.split()))
    lottoMatrix.append(lotto_numbers)
    lotto_numbers = []

# Take lotto matrix, create new scambled matrix.
n = 0
scrambled = []
firstScramble = []
while n < len(lottoMatrix):
    while len(firstScramble) < len(lottoMatrix[0]):
        number = lottoMatrix[randint(
            0, len(lottoMatrix) - 1)][randint(0, len(lottoMatrix[0]) - 1)]
        if number not in firstScramble:
            firstScramble.append(number)

    scrambled.append(firstScramble)
    firstScramble = []
    n += 1

# sorts the scrambled list into ascending order
final_lotto = []
for x in range(len(scrambled)):
    final_lotto.append(sorted(scrambled[x]))

# prints the final list on seperate lines
for x in range(len(final_lotto)):
    print(final_lotto[x])

# take list, scramble order.
# n = 0
# scrambled_numbers = []
# while n < len(lotto_numbers):
#	scrambled_numbers.append(lotto_numbers[randint(0,len(lotto_numbers)-1)])
#	n += 1
# print(scrambled_numbers)

# lotto = []
# for N in range(10):
#	for n in range(6):
#		lotto.append(randint(1,48))
#	print(lotto)
#	lotto = []
