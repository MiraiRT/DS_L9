class node:
    def __init__(self, data, l=None, r=None):
        self.data = data
        self.left = l
        self.right = r

    def __str__(self):
        return str(self.data)


def add(root, data):
    if root is None:
        root = node(data)
        return root
    else:
        if data < root.data:
            root.left = addi(root.left, data)
        else:
            root.right = addi(root.right, data)
    return root


def addi(root, data):
    if root is None:
        root = node(data)
    else:
        h = root
        while True:
            if data < h.data:
                if h.left is None:
                    h.left = node(data)
                    break
                else:
                    h = h.left
            else:
                if h.right is None:
                    h.right = node(data)
                    break
                else:
                    h = h.right
    return root


def inOrder(root):
    if root is not None:
        inOrder(root.left)
        print(root, end=' ')
        inOrder(root.right)


def printSideWay(root, lvl):
    if root is not None:
        printSideWay(root.right, lvl + 1)
        print(lvl * '   ', root.data)
        printSideWay(root.left, lvl + 1)


def height(root):
    if root is None:
        return 0
    else:
        return max(height(root.left), height(root.right)) + 1


def path(root, data):
    if root is None:
        print('Data Not Found')
    else:
        if data is root.data:
            print(root.data)
        elif data < root.data:
            print(root.data, end=' -> ')
            path(root.left, data)
        else:
            print(root.data, end=' -> ')
            path(root.right, data)


def search(root, data):
    if root is None:
        return None
    else:
        if data is root.data:
            return root
        elif data < root.data:
            return search(root.left, data)
        else:
            return search(root.right, data)


def depth(root, data):
    if search(root, data):
        if data is root.data:
            return 0
        elif data < root.data:
            return depth(root.left, data) + 1
        else:
            return depth(root.right, data) + 1
    else:
        return 0

l = [14, 4, 9, 7, 15, 3, 18, 16, 20, 5, 16]
print('Input : ', l)
r = None
for data in l:
    r = addi(r, data)
print('InOrder : ', end=' ')
inOrder(r)
print('\n')

print('PrintSideWay:')
printSideWay(r, 0)
print()

print('Height of', r.data, ':', height(r))
print()

d = 16
print('Path of', d, ':', end=' ')
path(r, d)
print()

d = 15
t = search(r, d)
print('Search', d, ':', t)
print()

d = 16
print('Depth of', d, ':', depth(r, d))
print()
