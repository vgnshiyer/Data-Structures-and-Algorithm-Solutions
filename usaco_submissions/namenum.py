import sys

'''
TASK: namenum
USER: Vignesh Iyer
LANG: Python
'''
hm = {'A':2, 'B': 2, 'C':2, 'J':5, 'K':5, 'L':5, 'T':8,'U':8,'V':8, 'D':3, 'E':3, 'F':3, 'M':6, 'N':6, 'O':6, 'W':9,'X':9,'Y':9, 'G':4, 'H':4, 'I':4, 'P':7, 'R':7, 'S':7}

# returns a list of names mapped with their appropriate id
def read_dictionary(filename) -> list:
    with open(filename, 'r') as f:
        valid_names = f.read().split()

    res = dict()
    for name in valid_names:
        idx = ""
        for char in name:
            try:
                idx += str(hm[char])
            except: pass
        res[name] = idx
    return res

def solve():
    idx = str(input())
    valid_ids = read_dictionary('dict.txt')
    ans = []
    
    for key, val in valid_ids.items():
        if val == idx:
            ans.append(key)
    
    if(ans == []):
      print("NONE")
    else:
      ans.sort()
      for name in ans:
          print(name)

if __name__ == "__main__":
    sys.stdin = open('namenum.in', 'r')
    sys.stdout = open('namenum.out', 'w')
    tc = 1
    while(tc):
        solve()
        tc -= 1