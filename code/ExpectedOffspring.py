def getDominentPhenotypePercentage(types):
    return (types[0] + types[1] + types[2] + types[3] * 0.75 + types[4] * 0.5 + types[5] * 0) * 2


if __name__ == "__main__":
    with open("../data/rosalind_iev.txt", 'r') as f:
        geneCounts = [int(count) for count in f.readline().strip().split(' ')]
        result = getDominentPhenotypePercentage(geneCounts)
        print(result)
