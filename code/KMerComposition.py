from utils import readFastaFormat
import itertools


def probaMendelMating(dominant, hetero, recess):
    total = dominant + hetero + recess
    mauso = total * (total - 1)
    couples = [
        dominant * (dominant - 1),
        dominant * hetero,
        dominant * recess,
        hetero * dominant,
        hetero * (hetero - 1) * 0.75,
        hetero * recess * 0.5,
        recess * dominant,
        recess * hetero * 0.5,
    ]
    return round(sum(couples) / mauso, 5)


if __name__ == "__main__":
    fastaDict = readFastaFormat("../data/rosalind_kmer.txt")
    string = list(fastaDict.values())[0]

    kmers = ["".join(x) for x in (itertools.product('ACGT', repeat=4))]
    seq = {kmerLabel: 0 for kmerLabel in kmers}

    for i in range(len(string) - 4 + 1):
        seq[string[i:i + 4]] += 1
    for i in kmers:
        print(seq[i], end=" ")
