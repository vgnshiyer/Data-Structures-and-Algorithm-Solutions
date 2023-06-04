def paintFill(image: list, r: int, c: int, color: str):
    if pixelOutOfBounds(image, r, c) or pixelRightlyColored(image, r, c, color):
        return

    image[r][c] = color
    paintFill(image, r, c+1, color)
    paintFill(image, r+1, c, color)
    paintFill(image, r, c-1, color)
    paintFill(image, r-1, c, color)

def pixelOutOfBounds(image: list, r: int, c: int) -> bool:
    if r >= len(image) or r < 0 or c >= len(image[0]) or c < 0:
        return True
    return False

def pixelRightlyColored(image: list, r: int, c: int, color: str) -> bool:
    return image[r][c] == color

def displayImage(image):
    for r in image:
        print(r)

if __name__ == '__main__':
    image = [
        ['R','R','R'],
        ['R','Y','W'],
        ['R', 'W', 'G']
    ]

    paintFill(image, 0, 0, 'G')

    displayImage(image)