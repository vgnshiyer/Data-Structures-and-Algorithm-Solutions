def printParens(n: int):
    openBrackets, closeBrackets = n, n
    
    def helper(string: str, openBrackets: int, closeBrackets: int):
        if openBrackets == 0 and closeBrackets == 0:
            print(string)
            return
        
        if openBrackets:
            helper(string + '(', openBrackets - 1, closeBrackets)

        if closeBrackets > openBrackets:
            helper(string + ')', openBrackets, closeBrackets - 1)

    helper('', openBrackets, closeBrackets)

if __name__ == '__main__':
    printParens(3)