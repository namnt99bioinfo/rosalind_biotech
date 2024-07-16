from math import factorial

def prob(k, n):
    p = []
    q = 2 ** k
    for i in range(n, (q + 1)):
        p.append(choose(q, i) * 0.25 ** i * 0.75 ** (q - i))
    return sum(p)


def choose(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


if __name__ == "__main__":
    with open("../data/rosalind_lia.txt", 'r') as f:
        numbers = [int(value) for value in f.readline().strip().split()]
        result = round(prob(numbers[0], numbers[1]), 3)
        print(result)
