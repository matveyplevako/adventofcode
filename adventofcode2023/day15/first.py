def get_hash(s):
    hash_val = 0
    for x in s:
        hash_val += ord(x)
        hash_val *= 17
        hash_val %= 256
    return hash_val


def main():
    ans = 0
    with open("input.txt") as inp:
        line = inp.readline().strip().split(",")
    for s in line:
        ans += get_hash(s)
    print(ans)


if __name__ == '__main__':
    main()
