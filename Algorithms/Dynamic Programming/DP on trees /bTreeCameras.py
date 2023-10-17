'''
This problem is a greedy problem. We make some observations.
1. If a node is a root node, there are three ways to monitor this node.
	a. place a camera on itself
	b. place a camera on one of its children
	
2. If a node is a leaf node, there are 2 ways to monitor it.
	a. place a camera on itself
	b. place a camera on its parent
	
3. If a node is somewhere inside the tree, there are 4 ways to monitor it.
	a. place a camera on itself
	b. place a camera on its root
	c. place a camera on one of its children
	
We can see that it is not benefitial for us to place a camera on the leaf nodes.

We define 4 states:
0 --> unmonitored node
1 --> monitored and has camera
2 --> monitored without a camera
inf --> leaf node

Another key observation is that it is benefitial for us to perform a bottom up search rather than a top down search. By doing a top down traversal we end up with more number of cameras.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def postorder(node):
            if not node: return 0, float('inf')

            left_cnt, left = postorder(node.left)
            right_cnt, right = postorder(node.right)

            state = min(left, right)
            total_cameras = left_cnt + right_cnt

            if state == 0: ## children unmonitored
                return total_cameras + 1, 1 ## place camera here

            if state == 1: ## children have camera
                return total_cameras, 2 ## place no camera and set as monitored

            return total_cameras, 0 ## note unmonitored

        return postorder(TreeNode(-1, root))[0] ## corner case --> tree with one node