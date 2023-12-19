workflows = {}


class Workflow:
    def __init__(self):
        self._flows = []

    def add(self, flow):
        self._flows.append(flow.split(":"))

    def process(self, x, m, a, s):
        for flow in self._flows:
            if len(flow) == 1:
                return workflows[flow[0]].process(x, m, a, s)
            else:
                if eval(flow[0]):
                    return workflows[flow[1]].process(x, m, a, s)


class AWorkflow(Workflow):
    def process(self, x, m, a, s):
        return True


class RWorkflow(Workflow):
    def process(self, x, m, a, s):
        return False


def main():
    ans = 0
    workflows["A"] = AWorkflow()
    workflows["R"] = RWorkflow()
    with open("input.txt") as inp:
        while line := inp.readline().strip():

            name, flows = line.split("{")
            flows = flows.rstrip("}")
            flows = flows.split(",")
            w = Workflow()
            for flow in flows:
                w.add(flow)
            workflows[name] = w

        for line in inp.readlines():
            line = line.strip()[1:-1]
            vals = line.split(",")
            xmas = {}
            for row in vals:
                x, val = row.split("=")
                xmas[x] = int(val)

            if workflows["in"].process(**xmas):
                ans += sum(xmas.values())

    print(ans)


if __name__ == '__main__':
    main()
