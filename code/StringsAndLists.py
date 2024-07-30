

if __name__ == "__main__":
    with open("../data/rosalind_init3.txt", 'r') as f:
        text = f.readline().strip()
        from1, to1, from2, to2 = f.readline().strip().split()
        print(text[int(from1):int(to1)+1], ' ', text[int(from2):int(to2)+1])
