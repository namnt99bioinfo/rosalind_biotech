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


def getProteinByRna(rna):
    proteinString = ''
    for i in range(0, len(rna), 3):
        aminoAcid = RNA_CODON_ADDRESS[rna[i:i + 3]]
        if aminoAcid == "STOP":
            break
        proteinString += aminoAcid
    return proteinString


if __name__ == "__main__":
    with open("../data/rosalind_prot.txt", 'r') as f:
        rna = f.readline().strip()
        result = getProteinByRna(rna)
        print(result)
