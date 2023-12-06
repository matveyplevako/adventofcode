def calc_dist(t, d):
    c = 0
    for h in range(1, t):
        if h * (t - h) > d:
            c += 1
    return c


def main():
    with open("input.txt") as inp:
        times = list(map(int, inp.readline().split(": ")[1].split()))
        req_dist = list(map(int, inp.readline().split(": ")[1].split()))
        ans = 1
        for i in range(len(times)):
            ans *= calc_dist(times[i], req_dist[i])
        print(ans)


if __name__ == '__main__':
    main()
