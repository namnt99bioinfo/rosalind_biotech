import math
def randomStrings(dna, gcContents):
    prob = 0
    results = []
    for gcContent in gcContents:
        prob = 0
        chance = {
            'A': (1 - gcContent) / 2,
            'T': (1 - gcContent) / 2,
            'C': gcContent / 2,
            'G': gcContent / 2,
        }
        for nucleotide in dna:
            prob += math.log10(chance[nucleotide])
        finalProb = round(prob, 3)
        results.append(finalProb)
    return results


if __name__ == "__main__":
    with open("../data/rosalind_prob.txt", 'r') as f:
        dna = f.readline().strip()
        gcContents = [float(value) for value in f.readline().strip().split(' ')]
        results = randomStrings(dna, gcContents)
        print(' '.join([str(r) for r in results]))

