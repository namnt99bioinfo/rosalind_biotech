import itertools


def orderingStringByLength(chars, number, acc='', res=[]):
    if number > 0:
        for c in chars:
            res.append(acc + c)
            orderingStringByLength(chars, number - 1, acc + c, res)
    return res

if __name__ == "__main__":
    with open("../data/rosalind_lexv.txt", 'r') as f:
        chars = f.readline().strip().replace(" ", "")
        number = int(f.readline())

        print("\n".join(orderingStringByLength(chars, number)))
