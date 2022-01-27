


if __name__ == '__main__':
    a = ModifiIterator([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
    b = ModifiIterator([1, 2, 3, 4, 5, 6, 7, 8, 9], 2)

    c = [i for i in a]  # [3, 6, 9]
    e = [i for i in b]  # [2, 4, 6, 8]

