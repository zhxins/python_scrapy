def tt(L):
    if len(L) > 0:
        minvalue = L[0]
        maxvalue = L[0]
        for x in L:
            if x < minvalue:
                minvalue = x
            if x > maxvalue:
                maxvalue = x

        return minvalue, maxvalue
    else:
        return 0, 0


def ss():
    name = input()
    print(name)

if __name__ == '__main__':
    list = [0, 1, 2, 3, 9, 8, 7]
    # res = tt(list)
    # print(res)

    ss()
