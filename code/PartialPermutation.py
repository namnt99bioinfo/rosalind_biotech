from math import factorial


def numPartialPerms(n, k):
    perm = (factorial(n) / factorial(n - k)) % 1000000
    return perm


if __name__ == "__main__":
    with open("../data/rosalind_pper.txt", 'r') as f:
        numbers = [int(value) for value in f.readline().strip().split()]
        print(numPartialPerms(numbers[0], numbers[1]))
