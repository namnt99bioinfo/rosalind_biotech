from utils import readFastaFormat


def findASplicedMotif(s1, s2):
    indices = []
    i = j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            indices.append(i + 1)
            j += 1
        i += 1
    return ' '.join(str(value) for value in indices)


if __name__ == "__main__":
    fastaDict = readFastaFormat("../data/rosalind_sseq.txt")
    strings = list(fastaDict.values())
    result = findASplicedMotif(strings[0], strings[1])
    print(result)
