from itertools import combinations

workflows = {}


def find_ranges(exclude, include=None):
    num_vals = {"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]}
    for i in exclude:
        letter = i[0]
        val = i[1:]
        if val[0] == ">":
            num_vals[letter][1] = min(num_vals[letter][1], int(val[1:]))
        else:
            num_vals[letter][0] = max(num_vals[letter][0], int(val[1:]))
    for i in include:
        letter = i[0]
        val = i[1:]
        if val[0] == ">":
            num_vals[letter][0] = max(num_vals[letter][0], int(val[1:]) + 1)
        else:
            num_vals[letter][1] = min(num_vals[letter][1], int(val[1:]) - 1)
    return num_vals


def dfs_search(ind, flow_name):
    exclude = []
    include = []
    if flow_name == "inp" and ind == len(workflows[flow_name]) - 1:
        return exclude, include
    elif ind == len(workflows[flow_name]) - 1:
        for name, row in workflows.items():
            for ind, item in enumerate(row):
                if item == [flow_name]:
                    _exclude, _include = dfs_search(ind, name)
                    exclude.extend(_exclude)
                    include.extend(_include)
                elif len(item) > 1 and item[1] == flow_name:
                    include.append(item[0])
                    _exclude, _include = dfs_search(ind, name)
                    exclude.extend(_exclude)
                    include.extend(_include)
    else:
        val = workflows[flow_name][ind + 1]
        exclude.append(val[0])
        _exclude, _include = dfs_search(ind + 1, flow_name)
        exclude.extend(_exclude)
        include.extend(_include)
    return exclude, include


def area(r):
    x = r['x'][1] - r['x'][0] + 1
    m = r['m'][1] - r['m'][0] + 1
    a = r['a'][1] - r['a'][0] + 1
    s = r['s'][1] - r['s'][0] + 1
    return x * m * a * s


def main():
    ans = 0
    all_ranges = []
    with open("input.txt") as inp:
        while line := inp.readline().strip():
            name, flows = line.split("{")
            flows = flows.rstrip("}")
            flows = flows.split(",")
            workflows[name] = []
            for flow in flows:
                flow = flow.split(":")
                workflows[name].append(flow)
            workflows[name] = workflows[name][::-1]

        for flow in workflows:
            for ind, item in enumerate(workflows[flow]):
                ranges = []
                if item == ["A"]:
                    exclude, include = dfs_search(ind, flow)
                    ranges = find_ranges(exclude, include)
                elif len(item) > 1 and item[1] == "A":
                    exclude, include = dfs_search(ind, flow)
                    include += [item[0]]
                    ranges = find_ranges(exclude, include)
                if ranges:
                    all_ranges.append(ranges)

    for r in all_ranges:
        ans += area(r)

    print(ans)


if __name__ == '__main__':
    main()
