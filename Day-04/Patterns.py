
def Pattern11(n):
    for i in range(1, 2 * n):
        start = i

        if i > n:
            start = 2 * n - i

        for j in range(1, start + 1):
            print("*", end="")

        print()


Pattern11(5)

def Pattern12(n):
    start = 1
    for i in range(0,n):
        if i % 2 == 0:
            start = 1
        else:
            start = 0
        for j in range(0,i+1):
            print(start, end="")
            start = 1 - start
        print()
Pattern12(5)
print("\n")

def Pattern13(n):
    #Number
    space = 2 * (n - 1)
    for i in range(1,n + 1):
       
    #Space
        for j in range(1,i + 1):
            print(j,end="")
        for j in range(space):
            print(" ",end="")
    #Number
        for k in range(i,0,-1):
            print(k,end="")
        space -=2
        print()

Pattern13(4)
print("\n")
num = 1
def Pattern14(n):

    num = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(num, end=" ")
            num += 1
        print()

Pattern14(5)

def Pattern15(n):
    for i in range(0, n + 1):
        for ch in range(65,65 + i):
            print(chr(ch), end="")
        print()
Pattern15(4)

print('\n')
def Pattern16(n):
    for i in range(0, n + 1):
        for ch in range(65,65 + (n - i)):
            print(chr(ch), end="")
        print()
Pattern16(4)