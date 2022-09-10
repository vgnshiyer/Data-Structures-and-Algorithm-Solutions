"""
TASK: fracdec
USER: Vignesh Iyer
LANG: PYTHON3
"""
from decimal import *
getcontext().prec = 100

def read_input(filename):
  global n
  global d
  with open(filename, 'r') as fin:
      n,d = tuple(map(int, fin.readline().strip().split()))

def get_first_occurrence(c, i, d):
  for j in range(i, len(d)):
    if(d[j] == c):
      return j
  return -1

def get_repeated_seq(d):
  l = len(d)
  for i in range(l):
    if(d[i] == '.'):
      break
  i += 1
  
  for j in range(i, l):
    start = j
    end = get_first_occurrence(d[j], start+1, d)
    if(end == -1):
      continue
    found = True
    cnt = 0
    for k in range(start, end):
      if(end + cnt < l and d[k] != d[end + cnt]):
        found = False  
        break
      cnt += 1
    if(found):
      ans = d[:i] + d[i:start] 
      if(d[start:end] == '0'):
        return ans
      return ans + '(' + d[start:end] + ')'
  return d

def solve(fout):
  if(n%d == 0):
    ans = str(n/d)
  else:
    ans = str(Decimal(n/d))
    ans = get_repeated_seq(ans)
  
  for i in range(len(ans)):
    fout.write(ans[i])
    if((i > 0 and i%75 == 0) or i == len(ans)-1):
      fout.write('\n')

filename = 'fracdec'
read_input(filename+'.in')

## output
with open(filename+'.out', 'w') as fout:
  solve(fout)