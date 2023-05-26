lst = [1,2,3]
lstIter = iter(lst)

class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)
    
    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()
    

# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    a1 = Node(3)
    a2 = Node(4)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(a1)
    child2.add_child(a2)
    # Outputs Node(1), Node(2)
    for ch in root:
        print(ch)