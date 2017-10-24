class node:
    def __init__(self, data, l=None, r=None):
        self.data = data
        self.left = l
        self.right = r

    def __str__(self):
        return str(self.data)


def addi(root, data):
    if root is None:
        root = node(data)
        return root
    else:
        if data < root.data:
            root.left = addi(root.left, data)
        else:
            root.right = addi(root.right, data)
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
        print('Invalid Data')
    else:
        if data is root.data:
            print(root.data)
        elif data < root.data:
            print(root.data, end=' -> ')
            path(root.left, data)
        else:
            print(root.data, end=' -> ')
            path(root.right, data)


l = [14, 4, 9, 7, 15, 3, 18, 16, 20, 5, 16]
print('Input : ', l)
r = None
for ele in l:
    r = addi(r, ele)
print('')
print('InOrder : ', end=' ')
inOrder(r)
print('\n')

print('printSideWay:')
printSideWay(r, 0)
print()

print('height of', r.data, '=', height(r))
print()

d = 5
print('path:', d, '=', end=' ')
path(r, d)
print()
