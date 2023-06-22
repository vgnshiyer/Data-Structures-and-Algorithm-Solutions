## BST sequences

from typing import List
import unittest

class TreeNode:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None
    
def bst_sequences(root: TreeNode):
    def visit(roots: List):
        output = []
        for root in roots:
            choices = [choice for choice in roots if choice != root]
            if root.left:
                choices.append(root.left)
            if root.right:
                choices.append(root.right)

            if len(choices) > 0:
                sequences = visit(choices)
                print(sequences)
                for sequence in sequences:
                    output.append([root.value] + sequence)
            else:
                output.append([root.value])
        return output
    
    return visit([root])

def bst_sequences2(root: TreeNode):
    if not root: return [[]]

    leftSequences = bst_sequences2(root.left)
    rightSequences = bst_sequences2(root.right)

    for left in leftSequences:
        for right in rightSequences:
            allSequences = []
            weave(left, right, [], allSequences)
    
    for sequence in allSequences: sequence.insert(0, root.value)

    return allSequences

def weave(left, right, prefix, result):
    if not left or not right:
        result.append(prefix + left + right)
        return

    leftHead = left.pop(0)
    prefix.append(leftHead)
    weave(left, right, prefix, result)
    prefix.pop()
    left.insert(0, leftHead)

    rightHead = right.pop(0)
    prefix.append(rightHead)
    weave(left, right, prefix, result)
    prefix.pop()
    right.insert(0, rightHead)

class BSTTests(unittest.TestCase):
    @staticmethod
    def create_tree() -> TreeNode:
        node = TreeNode(1)
        node.left = TreeNode(2)
        node.right = TreeNode(3)
        node.right.right = TreeNode(4)
        return node

    def test_bst_sequences(self):
        root = BSTTests.create_tree()
        sequences = bst_sequences2(root)
        print(sequences)
        actual_result = set(tuple(sequence) for sequence in sequences)
        expected_result = set(tuple(item) for item in [[1,2,3,4], [1,3,2,4], [1,3,4,2]])
        self.assertSetEqual(actual_result, expected_result)
