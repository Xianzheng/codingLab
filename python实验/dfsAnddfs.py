def getX():

    i = 0

    while i < 10:
        yield i
        i += 1

c = getX()
print(next(c))

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
        if self is None:
            return
        lst = []
        print(self)
        lst.append(self)
        for i in self._children:
            
            i.depth_first()

    def bfs(self):
        lst = []
        lst.append(self)
        seen = set()
        seen.add(self)
        while lst:
           node = lst.pop(0)
           for i in node._children:
               if i not in seen:
                   lst.append(i)
           print(node)

    
    def depth_first1(self):
        if self is None:
            return
        
        yield from self._children.de

        

    
               
                   
def fab(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b      # 使用 yield
        # print b 
        a, b = b, a + b 
        n = n + 1


lst = [1,2,3]

def t(lst):
    yield from lst

for i in t(lst):
    print(i)
 
print(list(fab(100)))

# # Example
# if __name__ == '__main__':
#     root = Node(0)
#     child1 = Node(1)
#     child2 = Node(2)
#     root.add_child(child1)
#     root.add_child(child2)
#     child1.add_child(Node(3))
#     child1.add_child(Node(4))
#     child2.add_child(Node(5))

#     root.bfs()