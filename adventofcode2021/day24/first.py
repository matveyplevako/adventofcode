def rec_search(a, b, c, ind, num, stack):
    if a[ind] == 1:
        for i in range(9, 0, -1):
            res = rec_search(a, b, c, ind + 1, num + [i], stack + [(i, c[ind])])
            if res:
                return res
    else:
        w_old, c_old = stack.pop()
        w_new = w_old + c_old + b[ind]
        if w_new > 9:
            return
        if ind == len(a) - 1:
            return num + [w_new]
        res = rec_search(a, b, c, ind + 1, num + [w_new], stack.copy())
        return res


def main():
    inst_list = []
    with open("input.txt") as inp:
        for line in inp.readlines():
            inst_list.append(line.split())

    a = [int(x[-1]) for x in inst_list[4::18]]
    b = [int(x[-1]) for x in inst_list[5::18]]
    c = [int(x[-1]) for x in inst_list[15::18]]
    print(a)
    print(b)
    print(c)
    print(''.join(map(str, rec_search(a, b, c, 0, [], []))))


if __name__ == '__main__':
    main()
