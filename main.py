

def i(items=[]):
    items.append(1)
    return items


if __name__ == '__main__':
    a = i()
    b = i()
    c = i([0])

    print(a, b, c)
