# A = T and G = C


def main():
    with open("rosalind_revc.txt", 'r') as f:
        with open("answer.txt", 'w') as wf:
            dna = f.read()
            # wf.write(reverse_complement(dna))
            print(reverse_complement(dna))


def reverse_complement(string):
    string = string.replace('A', 't').replace('T', 'a').replace(
        'C', 'g').replace('G', 'c').upper()[::-1]
    return string

    # return string[::-1].translate(str.maketrans('ACGT', 'TGCA'))

    # new_string = ''
    # for c in string:
    #     if c == 'A':
    #         new_string += 'T'
    #     elif c == 'T':
    #         new_string += 'A'
    #     elif c == 'G':
    #         new_string += 'C'
    #     elif c == 'C':
    #         new_string += 'G'
    # return new_string[::-1]


main()

'''
Better workaround
from string import maketrans
s = 'AAAACCCGGT'
print(s[::-1].translate(maketrans('ACGT', 'TGCA')))
'''
