
def countNu(dna):
    countA = dna.count("A")
    countC = dna.count("C")
    countG = dna.count("G")
    countT = dna.count("T")
    return countA, countC, countG, countT

if __name__ == "__main__":
    with open("../data/rosalind_dna.txt", 'r') as f:
        dna = f.readline().strip()
        print(dna)
        countA, countC, countG, countT = countNu(dna)
        print(countA, countC, countG, countT)
