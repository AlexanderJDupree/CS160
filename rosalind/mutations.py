

def main():

    with open("rosalind_hamm.txt", 'r') as f:
        with open("answer.txt", 'w') as wf:
            dna1 = f.readline()
            dna2 = f.readline()
            print(count_diff(dna1, dna2))


def count_diff(string1, string2):

    diff = 0
    for x, y in zip(string1, string2):
        if x != y:
            diff += 1
    return diff


main()
