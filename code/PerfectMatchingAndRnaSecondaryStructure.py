from utils import readFastaFormat
from math import factorial

if __name__ == "__main__":
    fastaDict = readFastaFormat("../data/rosalind_pmch.txt")
    seq_string = list(fastaDict.values())[0]

    auPairs = seq_string.count("A")
    gcPairs = seq_string.count("G")
    print(factorial(auPairs) * factorial(gcPairs))