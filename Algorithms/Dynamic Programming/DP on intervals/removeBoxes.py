'''
## Reference: https://leetcode.com/problems/remove-boxes/solutions/1402561/c-java-python-top-down-dp-clear-explanation-with-picture-clean-concise/?envType=list&envId=rc5rvbnt
Given a range in an array, we have 2 options to choose from

eg. 2 2 2 3 4 5 2 2 1

Option 1: Select boxes 0, 1 and 2 and remove them right away.

         2 2 2 3 4 5 2 2 1
         _____  <- end it here
         cur_score = 3*3 + dp(3, 8, 0)
         
Option 2: Try to extend the range of boxes with color 2

         2 2 2 3 4 5 2 2 1
         _____       _____ <- join these two
         
         cur_score = dp(3, 5, 0) + dp(6, 8, 3)  
         
Return the maximum of the two options

State: [i, j, k]
         i : start of the range
         j : end of the range
         k : consecutive boxes found of the same color 
'''
 def removeBoxes(self, boxes: List[int]) -> int:
     def dfs(i, j, k, dp):
         if i > j: return 0

         if (i, j, k) in dp: return dp[(i, j, k)]

         l, r = i, j
         consec_len = k

         while l + 1 <= r and boxes[l] == boxes[l + 1]:
             l += 1
             consec_len += 1

         ans = ((consec_len+1) ** 2) + dfs(l + 1, j, 0, dp) ## end sequence here

         ## try to continue the sequence
         for m in range(l + 1, r + 1):
             if boxes[m] == boxes[l]:
                 ans = max(ans, dfs(l + 1, m - 1, 0, dp) 
                                 + dfs(m, j, consec_len + 1, dp))
         dp[(i, j, k)] = ans
         return ans

     return dfs(0, len(boxes) - 1, 0, {})
         