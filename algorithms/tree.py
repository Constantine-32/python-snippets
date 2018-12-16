#!/usr/bin/env python

class Node(object):
  def __init__(self, val=None, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def preorder(tree):
  if not tree: return
  print(tree.val, end=' ')
  preorder(tree.left)
  preorder(tree.right)


def inorder(tree):
  if not tree: return
  inorder(tree.left)
  print(tree.val, end=' ')
  inorder(tree.right)


def postorder(tree):
  if not tree: return
  postorder(tree.left)
  postorder(tree.right)
  print(tree.val, end=' ')


def main():
  tree = Node('F')
  tree.left = Node('B')
  tree.left.left = Node('A')
  tree.left.right = Node('D')
  tree.left.right.left = Node('C')
  tree.left.right.right = Node('E')
  tree.right = Node('G')
  tree.right.right = Node('I')
  tree.right.right.left = Node('H')

  print('\npreorder')
  preorder(tree)
  print('\ninorder')
  inorder(tree)
  print('\npostorder')
  postorder(tree)


if __name__ == '__main__':
  main()
