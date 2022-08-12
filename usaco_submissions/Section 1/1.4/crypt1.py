"""
TASK: crypt1
USER: Vignesh Iyer
LANG: PYTHON3
"""

ans = 0

def read_input(filename):
    global n
    global nums
    with open(filename, 'r') as fin:
        n = int(fin.readline().strip())
        nums = fin.readline().strip().split(' ')
        nums = sorted(nums)

def is_valid(num):
  for x in str(num):
    if x not in nums:
      return False
  return True

def compute(a, b):
  global ans
  if(not is_valid(a) or not is_valid(b)): return
  unit = int(str(b)[1])
  tens = int(str(b)[0])
  partial_prod1 = unit*a
  partial_prod2 = tens*a
  final_prod = b*a

  if(len(str(partial_prod1)) > 3 or len(str(partial_prod2)) > 3): return

  if(is_valid(a) and is_valid(b) and is_valid(partial_prod1) and is_valid(partial_prod2) and is_valid(final_prod)):
    ans += 1

def solve(fout):
    num1 = int("".join(nums[0]*3))
    num1_end = int("".join(nums[n-1]*3))
    num2 = int("".join(nums[0]*2))
    num2_end = int("".join(nums[n-1]*2))
    for a in range(num1, num1_end + 1):
      for b in range(num2, num2_end + 1):
        compute(a,b)
    fout.write(str(ans)+'\n')

filename = 'crypt1'
read_input(filename+'.in')

## output
with open(filename+'.out', 'w') as fout:
    solve(fout)