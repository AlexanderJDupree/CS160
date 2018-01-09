

def main():
    with open("rosalind_rna.txt", 'r') as f:
        with open("answer.txt", 'w') as wf:
            wf.write("U".join(f.read().split("T")))


main()
