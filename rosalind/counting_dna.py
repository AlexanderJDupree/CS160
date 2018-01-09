

def main(s):
    # return s.count("A"), s.count("G"), s.count("C"), s.count("T")
    print(*map(s.count, "ACGT"))


with open("rosalind_dna.txt", 'r') as f:
    with open("answer.txt", 'w') as wf:
        f_contents = f.read()
        answer = str(main(f_contents)).strip("()")
        wf.write(answer.replace(",", ''))
        print(main(f_contents))
