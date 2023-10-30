class Node:
    left = None
    right = None
    parent = None

    def __str__(self):
        return f"[{self.left},{self.right}]"

    def explode_left(self, num):
        parent = self.parent
        if parent is None:
            return
        if self == parent.left:
            parent.explode_left(num)
        elif type(parent.left) == int:
            parent.left += num
        else:
            node = parent.left
            while type(node.right) != int:
                node = node.right
            node.right += num

    def explode_right(self, num):
        parent = self.parent
        if parent is None:
            return
        if self == parent.right:
            parent.explode_right(num)
        elif type(parent.right) == int:
            parent.right += num
        else:
            node = parent.right
            while type(node.left) != int:
                node = node.left
            node.left += num

    def explode(self):
        self.explode_right(self.right)
        self.explode_left(self.left)
        parent = self.parent
        if parent.left == self:
            parent.left = 0
        else:
            parent.right = 0

    def search_for_explode(self, level=0):
        if level >= 4 and all([type(self.left) == int, type(self.right) == int]):
            self.explode()
            return True
        if type(self.left) != int:
            if self.left.search_for_explode(level + 1):
                return True
        if type(self.right) != int:
            if self.right.search_for_explode(level + 1):
                return True

    @staticmethod
    def split_node(node, parent, direction):
        num = node
        node = Node()
        node.left = num // 2
        node.right = num // 2 + num % 2
        node.parent = parent
        if direction == "left":
            parent.left = node
        else:
            parent.right = node

    def search_for_split(self):
        if type(self.left) == int and self.left > 9:
            self.split_node(self.left, self, "left")
            return True
        elif type(self.left) != int:
            if self.left.search_for_split():
                return True
        if type(self.right) == int and self.right > 9:
            self.split_node(self.right, self, "right")
            return True
        elif type(self.right) != int:
            if self.right.search_for_split():
                return True

    def magnitude(self):
        if type(self.left) == int:
            left = self.left
        else:
            left = self.left.magnitude()
        if type(self.right) == int:
            right = self.right
        else:
            right = self.right.magnitude()
        return 3 * left + 2 * right


def parse(number, parent=None):
    if type(number) == int:
        return number
    if type(number) == list:
        left, right = number
        node = Node()
        node.parent = parent
        node.left = parse(left, node)
        node.right = parse(right, node)
        return node


def process(node):
    while node.search_for_explode() or node.search_for_split():
        ...


def add(node1, node2):
    node = Node()
    node.left = node1
    node.right = node2
    node1.parent = node
    node2.parent = node
    process(node)
    return node


def main():
    with open("input.txt") as inp:
        number = eval(inp.readline())
        node = parse(number)
        for line in inp.readlines():
            node = add(node, parse(eval(line)))
    print(node.magnitude())


if __name__ == '__main__':
    main()
