"""this is to find specific soltution"""

def answer(n):
    """this finds the the difference between the sum of the squares of the first ten natural numbers and the square of the sum"""
    n=n
    s = ((n) * (n + 1) * (2 * n + 1)) / 6
    sl = ((n * (n + 1)) / 2) ** 2
    return int(sl - s)

if __name__ == "__main__":
    print((answer(100)))
