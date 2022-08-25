"""
TASK: zerosum
USER: Vignesh Iyer
LANG: PYTHON3
"""

def read_input(filename):
    global n
    with open(filename, 'r') as fin:
        n = int(fin.readline().strip())

answer = []

def dfs(seq, num):
    if(num == n):
        sum_ = eval(seq.replace(' ',''));
        if(sum_ == 0):
            answer.append(seq);
        return;
    
    dfs(seq+'+'+str(num+1), num+1)
    dfs(seq+'-'+str(num+1), num+1)
    dfs(seq+' '+str(num+1), num+1)

def solve(fout):
    dfs('1', 1)
    answer.sort()
    for seq in answer:
        fout.write(seq+'\n')

filename = 'zerosum'
read_input(filename+'.in')

## output
with open(filename+'.out', 'w') as fout:
    solve(fout)