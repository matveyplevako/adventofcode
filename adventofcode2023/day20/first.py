modules = {}


class Broadcaster:
    def __init__(self, name, outputs):
        self.name = name
        self.outputs = outputs

    def process(self, _, signal, queue):
        for inp in self.outputs:
            queue.append((self.name, signal, inp))


class FlipFlop:
    def __init__(self, name, outputs):
        self.name = name
        self.outputs = outputs
        self.state = 0

    def process(self, _, signal, queue):
        if signal:
            return
        if not signal:
            self.state = (self.state + 1) % 2
        for inp in self.outputs:
            queue.append((self.name, self.state, inp))


class Conjunction:
    def __init__(self, name, outputs):
        self.name = name
        self.outputs = outputs
        self.states = {}

    def add_input(self, inp):
        self.states[inp] = 0

    def process(self, input_from, signal, queue):
        self.states[input_from] = signal
        res_signal = 1
        if set(self.states.values()) == {1}:
            res_signal = 0
        for inp in self.outputs:
            queue.append((self.name, res_signal, inp))


def main():
    with open("input.txt") as inp:
        for line in inp.readlines():
            line = line.strip()
            name, pass_to_modules = line.split(" -> ")
            pass_to_modules = pass_to_modules.split(", ")

            if name == "broadcaster":
                b = Broadcaster("broadcaster", pass_to_modules)
                modules["broadcaster"] = b
            else:
                prefix, name = name[0], name[1:]
                if prefix == "%":
                    modules[name] = FlipFlop(name, pass_to_modules)
                elif prefix == "&":
                    modules[name] = Conjunction(name, pass_to_modules)

    for name in modules:
        for sub_name in modules[name].outputs:
            if sub_name in modules and type(modules[sub_name]) == Conjunction:
                modules[sub_name].add_input(name)

    low, high = 0, 0
    for i in range(1000):
        q = [("button", 0, "broadcaster")]
        while q:
            previous, signal, name = q.pop(0)
            if signal:
                high += 1
            else:
                low += 1

            if name not in modules:
                continue
            modules[name].process(previous, signal, q)
            print(*q, sep='\n')
            print('----')
        print("ANOTHER ONE")

    print(high, low)
    print(high * low)


if __name__ == '__main__':
    main()
