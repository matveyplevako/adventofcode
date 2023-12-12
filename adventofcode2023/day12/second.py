from functools import cache


@cache
def search(s, rec, pos, count, matched):
    if pos == len(s):
        return len(rec) == matched
    elif s[pos] == '#':
        return search(s, rec, pos + 1, count + 1, matched)
    elif s[pos] == '.' or matched == len(rec):
        if matched < len(rec) and count == rec[matched]:
            return search(s, rec, pos + 1, 0, matched + 1)
        elif count == 0:
            return search(s, rec, pos + 1, 0, matched)
        else:
            return 0
    else:
        hash_count = search(s, rec, pos + 1, count + 1, matched)
        dot_count = 0
        if count == rec[matched]:
            dot_count = search(s, rec, pos + 1, 0, matched + 1)
        elif count == 0:
            dot_count = search(s, rec, pos + 1, 0, matched)
        ret = hash_count + dot_count
    return ret


def main():
    ans = 0
    with open("input.txt") as inp:
        for row in inp.readlines():
            spring, rec = row.split()
            _rec = list(map(int, rec.split(",")))
            rec = []
            [rec.extend(_rec) for _ in range(5)]
            rec = tuple(rec)
            spring = '?'.join([spring] * 5) + '.'
            ans += search(spring, rec, 0, 0, 0)
    print(ans)


if __name__ == '__main__':
    main()
