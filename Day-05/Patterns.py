
def pattern7(n):
    for i in range(1, n + 1):

        # Left spaces
        for space in range(n - i):
            print(" ", end="")

        # Alphabets
        ch = 'A'
        breakpoint = (2 * i + 1) // 2

        for star in range(2 * i - 1):
            print(ch, end="")
            ch = chr(ord(ch) + 1)

        # New line
        print()

pattern7(5)
