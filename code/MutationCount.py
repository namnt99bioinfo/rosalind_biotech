
def countMutationPoint(orgStrand, compareStrand):
    count = 0
    if len(orgStrand) == len(compareStrand):
        for i in range(len(orgStrand)):
            if orgStrand[i] != compareStrand[i]:
                count += 1
    return count


if __name__ == "__main__":
    with open("../data/rosalind_hamm.txt", 'r') as f:
        orgStrand = f.readline().strip()
        compareStrand = f.readline().strip()
        print(countMutationPoint(orgStrand, compareStrand))
