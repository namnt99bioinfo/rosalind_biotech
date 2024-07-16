import itertools

def permutation(number):
    list1 = []
    for i in range(number):
        list1.append(i + 1)

    list2 = list(itertools.permutations(list1, number))

    print(len(list2))
    for l in list2:
        print(" ".join([str(i) for i in l]))


if __name__ == "__main__":
    with open("../data/rosalind_perm.txt", 'r') as f:
        number = int(f.readline())
        permutation(number)

