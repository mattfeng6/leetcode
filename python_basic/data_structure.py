# https://www.geeksforgeeks.org/python-data-structures-and-algorithms/#

# List
if True:
    # allows different types of elements
    List = [1, 2, 3, 4.2, "test"]
    print(List)

    # print the first element of list
    print(List[0])

    # print the last element of list
    print(List[-1])
        
    # print the third last element of list
    print(List[-3])

print("----------------")

# Tuple
if True:
    # similar to list but is immutable
    Tuple = ("test1", "test2")
    print(Tuple)

    # create a tuple using list
    list1 = [1, 2, 3, 4]
    Tuple2 = tuple(list1)
    print(Tuple2)

    # access element from last
    print(Tuple[-1])

print("----------------")

# Set
if True:
    # mutable collection of data
    # does not allow any duplication
    Set = set([1, 2, 3, 2, 3, 4, 5, 5])
    print(Set)

print("----------------")

# String
if True:
    # immutable array of bytes representing Unicode characters
    # modifying a string will result in creating a new copy
    String = "Hello World!"
    print(String)

print("----------------")

# Dictionary
if True:
    # unordered collection of data
    # format of key : value pair
    Dict = {'Name': 'test', 1: [1, 2, 3]}
    print(Dict)

    # access an element using key
    print(Dict['Name'])

    # access an element using get()
    print(Dict.get(1))

    # use Dictionary comprehension to create
    Dict2 = {x: x**2 for x in [1, 2, 3, 4, 5]}
    print(Dict2)

print("----------------")

# Matrix
if True:
    # 2D array where each element is of strictly the same size
    import numpy as np
    a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    m = np.reshape(a, (3, 3))
    print(m)

    # add element
    m = np.append(m, [[1, 3, 5]], 0)
    print(m)

    # delete element
    m = np.delete(m, [1], 0)
    print(m)

print("----------------")

# Linked List
if True:
    # Elements are linked using pointers
    class Node:
    
        def __init__(self, data):
            self.data = data
            self.next = None

    class LinkedList:

        def __init__(self):
            self.head = None
    
    if __name__ == '__main__':
        llist = LinkedList()

        llist.head = Node(1)
        second = Node(2)
        third = Node(3)

        llist.head.next = second
        second.next = third

    # traversal
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

print("----------------")

# Stack
if True:
    # last in, first out
    stack = []

    stack.append(1)
    stack.append(2)
    stack.append(3)

    print(stack)
    print(stack.pop())
    print(stack)

print("----------------")

# Queue
if True:
    # first in, first out
    queue = []

    queue.append(1)
    queue.append(2)
    queue.append(3)

    print(queue)
    print(queue.pop(0))
    print(queue)

# Priority Queue
if True:
    # each data/value has a certain priority
    class PriorityQueue(object):
        def __init__(self):
            self.queue = []

        def __str__(self):
            return ' '.join([str(i) for i in self.queue])
        
        def isEmpty(self):
            return len(self.queue) == 0
        
        def insert(self, data):
            self.queue.append(data)

        def delete(self):
            try:
                max = 0
                for i in range(len(self.queue)):
                    if self.queue[i] > self.queue[max]:
                        max = i
                item = self.queue[max]
                del self.queue[max]
                return item
            except IndexError:
                print()
                exit()

    myQueue = PriorityQueue()
    myQueue.insert(3)
    myQueue.insert(5)
    myQueue.insert(1)

    print(myQueue)
    while not myQueue.isEmpty():
        print(myQueue.delete())

print("----------------")

# Binary Tree
if True:
    # each elements can have at most two children
    class Node:
        def __init__(self, key):
            self.left = None
            self.right = None
            self.val = key

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    def printInorder(root):
        if root:
            printInorder(root.left)
            print(root.val)
            printInorder(root.right)

    def printbreathfirstorder(root):
        if root is None:
            return
        
        queue = []
        queue.append(root)

        while(len(queue) > 0):
            print(queue[0].data)
            node = queue.pop(0)

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

print("----------------")

# Graph
if True:
    # consist of nodes(vertices) and edges
    print()
