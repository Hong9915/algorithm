import sys
input = sys.stdin.readline

N = int(input())

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

node_tree = {}

for _ in range(N):
    parent, left, right = input().strip().split()

    if parent not in node_tree:
        node_tree[parent] = Node(parent)
    if left != ".":
        node_tree[left] = Node(left)
        node_tree[parent].left = node_tree[left]
    if right != ".":
        node_tree[right] = Node(right)
        node_tree[parent].right = node_tree[right]

def preorder(node):
    if not node:
        return
    print(node.value, end='')  
    preorder(node.left)        
    preorder(node.right)      

def inorder(node):
    if not node:
        return
    inorder(node.left)         
    print(node.value, end='')  
    inorder(node.right)        

def postorder(node):
    if not node:
        return
    postorder(node.left)       
    postorder(node.right)      
    print(node.value, end='')  


root = node_tree['A']


preorder(root)
print()
inorder(root)
print()
postorder(root)
print()
