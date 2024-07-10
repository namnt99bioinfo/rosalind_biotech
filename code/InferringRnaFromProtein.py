RNA_CODON_ADDRESS = {"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
                     "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
                     "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
                     "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
                     "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
                     "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
                     "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
                     "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
                     "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
                     "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
                     "UAA": "STOP", "CAA": "Q", "AAA": "K", "GAA": "E",
                     "UAG": "STOP", "CAG": "Q", "AAG": "K", "GAG": "E",
                     "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
                     "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
                     "UGA": "STOP", "CGA": "R", "AGA": "R", "GGA": "G",
                     "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
                     }


def codonFrequencies():
    frequencies = {}
    for key, value in RNA_CODON_ADDRESS.items():
        if not value in frequencies:
            frequencies[value] = 0
        frequencies[value] += 1
    return frequencies


def possibleRnaStrings(protein):
    frequentCodons = codonFrequencies()
    possible = frequentCodons['STOP']

    for aa in protein:
        possible *= frequentCodons[aa]
    return possible % 1000000


if __name__ == "__main__":
    with open("../data/rosalind_mrna.txt", 'r') as f:
        proteinString = f.readline().strip()
        result = possibleRnaStrings(proteinString)
        print(result)
