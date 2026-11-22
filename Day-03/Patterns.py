def Pattern1(n):
    for i in range(n):
        for j in range(1, n + 1):
            print("*", end="")
        print()


Pattern1(5)

def pattern2(n):
    for i in range(1,n+1):
        for j in range(i):
            print("*",end="")
        print()
pattern2(5)

def pattern3(n):
    for i in range(1,n+1):
        for j in range(1, i+ 1):
            print(j ,end=" ")
        print()
pattern3(5)

def pattern4(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i,end=" ")
        print()

pattern4(5)

print("Pattern 5")
def pattern5(n):
    for i in range(1,n+1):
        for j in range(1,n - i +2):
            print("* ",end="")
        print()
pattern5(5)

def pattern6(n):
    for i in range(1,n + 1):
        for j in range(1, n - i + 2):
            print(j, end="")
        print()
pattern6(5)

print("Pattern 7")

def pattern7(n):
    for i in range(1, n + 1):
        # Left spaces
        for space in range(n - i):
            print("-", end="")

        # Stars
        for star in range(2 * i - 1):
            print("*", end="")

        # New line
        print()

pattern7(5)

print("Pattern 8")
def pattern8(n):
    for i in range(n):
        #Spaces
        #Start
        #Spaces
        for space in range(i):
            print(" ", end="")

        for stars in range(2 * n - (2* i + 1) ):
            print("*", end="")

        #Stars
        for space in range(i):
                    print(" ", end="")

        print()
pattern8(5)


def pattern9(n):
      for i in range(1, n + 1):
            # Left spaces
            for space in range(n - i):
                print(" ", end="")
    
            # Stars
            for star in range(2 * i - 1):
                print("*", end="")
    
            # New line
            print()
      for k in range(1, n + 1):
            for space in range(k):
                      print(" ", end="")
          
            for stars in range(2 * n - (2* k + 1) ):
                    print("*", end="")
          
                  #Stars
            for space in range(k):
                    print(" ", end="")
            print()

pattern9(5)   

def pattern10(n):
     for i in range(n):
          for j in range(i + 1):
                print("*", end="") 
          print()
     for k in range(n):
            for j in range(n  - k):
                print("*", end="") 
            print()
pattern10(5)