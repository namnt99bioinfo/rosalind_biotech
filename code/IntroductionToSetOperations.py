import math

def union(a, b):
    return a | b

def intersection(a, b):
    return a & b

def difference(a, b):
    return a - b

def complement(u, a):
    return u - a


if __name__ == "__main__":
    with open("../data/rosalind_seto.txt", 'r') as f:
        n = int(f.readline().strip())
        a0 = f.readline().strip()
        b0 = f.readline().strip()

        for i in ['{', '}']:
            a0 = a0.replace(i, '')
            b0 = b0.replace(i, '')

        a = set(int(i) for i in a0.split(', '))
        b = set([int(i) for i in b0.split(', ')])

        u = set({})
        for i in range(n):
            u.add(i + 1)
        # print(a, b, u)
        print(union(a, b))
        print(intersection(a, b))
        print(difference(a, b))
        print(difference(b, a))
        print(complement(u, a))
        print(complement(u, b))
