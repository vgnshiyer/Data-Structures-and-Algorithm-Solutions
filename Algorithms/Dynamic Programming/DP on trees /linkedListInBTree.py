## DFS Solution
def compare(self, head, root):
    if not head: return True
    if not root: return False

    if root.val == head.val: return self.compare(head.next, root.left) or self.compare(head.next, root.right)

    return False

def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
    if not head: return True
    if not root: return False
    if root.val == head.val and self.compare(head, root): return True
    return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

### KMP Search solution
def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
  pattern = []
  while head:
      pattern.append(head.val)
      head = head.next

  m = len(pattern)
  j = 0
  lps = [0] * m
  for i in range(1, m):
      if j > 0 and pattern[i] != pattern[j]: j = lps[j - 1]
      if pattern[i] == pattern[j]:
          j += 1
      lps[i] = j
  
  def kmpSearch(node, j):
      if j == len(pattern): return True
      if not node: return False
      while j > 0 and node.val != pattern[j]: j = lps[j - 1]
      if node.val == pattern[j]: j += 1
      return kmpSearch(node.left, j) or kmpSearch(node.right, j)

  return kmpSearch(root, 0)