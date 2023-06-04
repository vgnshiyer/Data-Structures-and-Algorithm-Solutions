def multiply(a: int, b: int) -> int:
    if a > b:
        a, b = b, a

    if a == 0: return 0
    if a == 1: return b

    partialProduct = multiply(a//2, b)
    if a & 1:
        return partialProduct + partialProduct + b
    return partialProduct + partialProduct

if __name__ == '__main__':
    print(multiply(3,2))