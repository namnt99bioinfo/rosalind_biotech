def numRabbits(month, age):
    generation = [0] * age
    generation[0], generation[1] = 0, 1

    for x in range(2, month):
        temp = list(generation)
        generation[0] = sum(generation[1:])  # number of new born
        for i in range(1, age):
            generation[i] = temp[i - 1]
    return sum(generation)


if __name__ == "__main__":
    with open("../data/rosalind_fibd.txt", 'r') as f:
        n, k = f.readline().strip().split(" ")
        print(numRabbits(int(n), int(k)))
