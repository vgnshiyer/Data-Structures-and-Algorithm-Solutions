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
                for sequence in sequences:
                    output.append([root.value] + sequence)
            else:
                output.append([root.value])
        return output
    
    return visit([root])

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
        sequences = bst_sequences(root)
        actual_result = set(tuple(sequence) for sequence in sequences)
        expected_result = set(tuple(item) for item in [[1,2,3,4], [1,3,2,4], [1,3,4,2]])
        self.assertSetEqual(actual_result, expected_result)
