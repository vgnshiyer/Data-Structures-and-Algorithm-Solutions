## 1.6 String compression

def compressString(string):
    n = len(string)
    compressedString = ''

    letter = string[0]
    freq = 1
    
    for i in range(1, n):
        if string[i] == string[i-1]:
            freq += 1
        else:
            compressedString += (letter + str(freq))
            freq = 1
            letter = string[i]

    compressedString += (letter + str(freq))
    return compressedString

if __name__ == '__main__':
    inp = 'aabcccccaaa'

    print(compressString(inp))