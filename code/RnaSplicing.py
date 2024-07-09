from utils import readFastaFormat

DNA_CODON_DICT = {
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
    'TAA': '-', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
    'TAG': '-', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
    'TGT': 'C', 'CGT': 'R', 'AGT': 'S', 'GGT': 'G',
    'TGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
    'TGA': '-', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
    'TGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
}


def slicingRna(orgDna, introns):
    protein = ''
    for intron in introns:
        orgDna = orgDna.replace(intron, '')
    for index in range(0, len(orgDna) - 2, 3):
        if DNA_CODON_DICT[orgDna[index:index + 3]] == '-':
            break
        protein += DNA_CODON_DICT[orgDna[index:index + 3]]
    return protein


if __name__ == "__main__":
    fastaDict = readFastaFormat("../data/rosalind_splc.txt")
    rnaList = list(fastaDict.values())
    dna, introns = rnaList[0], rnaList[1:]
    protein = slicingRna(dna, introns)
    print(protein)
