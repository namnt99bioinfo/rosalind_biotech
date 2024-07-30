import itertools


def sorting(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def findMax(arr):
    maxValue = arr[0]
    for value in arr:
        if value > maxValue:
            maxValue = value
    return maxValue


def recursion(value):
    if value == 0:
        return 0
    return recursion(value - 1) + value


def factory(value):
    if value == 0:
        return 1
    return value * factory(value - 1)


def fib(order):
    if order == 0:
        return 0
    if order == 1 or order == 2:
        return 1
    return fib(order - 1) + fib(order - 2)


# def translateRNAtoProtein(rna):
#     protein = ''
#     for i in range(0, len(rna), 3):
#         aa = RNA_CODON_ADDRESS[rna[i: i+ 3]]
#         if aa == 'STOP':
#             break
#         protein += aa
#     return protein

# map(str, positions) == str(x) for x in positions

def permutation(number):
    numbers = []
    for i in range(number):
        numbers.append(i + 1)

    list2 = list(itertools.permutations(numbers, number))
    print(len(list2))

    for i in list2:
        print(" ".join(map(str, i)))


def product(string, number):
    list1 = list(itertools.product(string, repeat=number))
    print('\n'.join([''.join(x) for x in list1]))

# def permutation2(number):
#     list1 = []
#     for i in range(number):
#         list1.append(i + 1)
#     list2 = list(itertools.permutations(list1, number))
#     print(len(list2))
#
#     print(' '.join(map(str, i) for i in list2))

if __name__ == "__main__":
    with open("../data/rosalind_iprb.txt", 'r') as f:
        dominant, hetero, recess = map(float, f.readline().strip().split(' '))

        print(sorting([64, 34, 25, 12, 22, 11, 90]))
        print(findMax([64, 34, 25, 12, 22, 11, 90]))
        print(recursion(8))
        print(factory(4))
        print(fib(10))
        product('ATGC', 3)
        permutation(4)
