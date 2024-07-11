from utils import readFastaFormat

if __name__ == "__main__":
    fastaDict = readFastaFormat("../data/rosalind_grph.txt")
    seq_string = list(fastaDict.values())
    seq_name = [name.replace('>', '') for name in list(fastaDict.keys())]

    min_length = 3

    for i in range(len(seq_string)):
        for j in range(len(seq_string)):
            if i != j:
                subfix_seq = seq_string[i][-min_length:]
                prefix_seq = seq_string[j][:min_length]

                if subfix_seq == prefix_seq:
                    print(seq_name[i], seq_name[j])
