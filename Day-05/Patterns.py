
def pattern17(n):
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

pattern17(5)

print('\n')


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

pattern19(5)

print("\n")

def pattern20(n):

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


pattern20(5)
print("\n")
def pattern21(n):
    for i in range(n):
        for j in range(n):
            if i==0 or i == n - 1 or j ==0 or j == n - 1:
                print("*",end="")
            else:
                print(" ",end="")
        print()
pattern21(4)

