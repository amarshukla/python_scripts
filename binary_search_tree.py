class Node:
  """
  class to create Node
  """

  def __init__(self, key):
    self.left = None
    self.right = None
    self.val = key

def insert(root, node):
  """
  Insert a new node to Binary Search Tree
  """

  if root is None:
    root = node
  else:
    if node.val > root.val:
      if root.right is None:
        root.right = node
      else:
        insert(root.right, node)
    else:
      if root.left is None:
        root.left = node
      else:
        insert(root.left, node)

def inorder_traversal(root):
  """
  Left -> root -> right traversal
  """

  if root:
    inorder_traversal(root.left)
    print(root.val)
    inorder_traversal(root.right)

def preorder_traversal(root):
  """
  Root -> Left -> Right
  """
  
  if root:
    print(root.val)
    preorder_traversal(root.left)
    preorder_traversal(root.right)

r = Node(50) 
insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80))

#inorder_traversal(r)
preorder_traversal(r)
