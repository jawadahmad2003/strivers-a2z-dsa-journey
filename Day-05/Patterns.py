
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

print('\n')
def pattern8(n):
    for i in range(1, n + 1):

        # Left spaces
        for space in range(i - 1):
            print(" ", end="")

        # Alphabets
        ch = 'A'
        for j in range(2 * (n - i) + 1):
            print(ch, end="")
            ch = chr(ord(ch) + 1)

        print()

pattern8(5)

print("\n")

def pattern18(n):
    for i in range(1, n + 1):

        # Spaces


        # Alphabets
        ch = chr(ord('A') + n - i)

        for j in range(i):
            print(ch, end=" ")
            ch = chr(ord(ch) + 1)

        print()

pattern18(5)


def pattern19(n):

    # Upper half
    for i in range(n):

        # Left stars
        for j in range(n - i):
            print("*", end="")

        # Spaces
        for j in range(2 * i):
            print(" ", end="")

        # Right stars
        for j in range(n - i):
            print("*", end="")

        print()

    # Lower half
    for i in range(n):

        # Left stars
        for j in range(i + 1):
            print("*", end="")

        # Spaces
        for j in range(2 * (n - i - 1)):
            print(" ", end="")

        # Right stars
        for j in range(i + 1):
            print("*", end="")

        print()


pattern19(5)
