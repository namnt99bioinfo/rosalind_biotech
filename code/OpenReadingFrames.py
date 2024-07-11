from utils import readFastaFormat

DNA_CODON_TABLE = {
    'TTT': 'F', 'CTT': 'L', 'ATT': 'I', 'GTT': 'V',
    'TTC': 'F', 'CTC': 'L', 'ATC': 'I', 'GTC': 'V',
    'TTA': 'L', 'CTA': 'L', 'ATA': 'I', 'GTA': 'V',
    'TTG': 'L', 'CTG': 'L', 'ATG': 'M', 'GTG': 'V',
    'TCT': 'S', 'CCT': 'P', 'ACT': 'T', 'GCT': 'A',
    'TCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
    'TCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
    'TCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
    'TAT': 'Y', 'CAT': 'H', 'AAT': 'N', 'GAT': 'D',
    'TAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
    'TAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
    'TAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
    'TGT': 'C', 'CGT': 'R', 'AGT': 'S', 'GGT': 'G',
    'TGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
    'TGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
    'TGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
}


def translateCodon(codon):
    protein = None
    if len(codon) == 3 and codon in DNA_CODON_TABLE:
        protein = DNA_CODON_TABLE[codon]
    return protein


def reverseComplement(dna):
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join([complement[nu] for nu in reversed(dna)])


def possibleProteinStrings(string):
    results = []
    indices = []

    # find start codon
    for i in range(len(string)):
        protein = translateCodon(string[i:i + 3])
        if protein == 'M':
            indices.append(i)

    # run from start codon and search to stop codon
    for i in indices:
        foundStop = False
        proteinString = ''

        for j in range(i, len(string), 3):
            protein = translateCodon(string[j:j + 3])

            if protein == 'Stop':
                foundStop = True
                break

            proteinString += protein

        if foundStop:
            results.append(proteinString)

    return results


if __name__ == "__main__":
    fastaDict = readFastaFormat("../data/rosalind_orf.txt")
    string = list(fastaDict.values())[0]

    possibleProteinA = possibleProteinStrings(string)
    possibleProteinB = possibleProteinStrings(reverseComplement(string))
    print("\n".join(set(possibleProteinA + possibleProteinB)))
