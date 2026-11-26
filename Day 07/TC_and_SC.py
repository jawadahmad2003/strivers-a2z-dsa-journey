"""
Time and Space Complexity
Last Updated :
31 Jul, 2025
Many times there are more than one ways to solve a problem with different algorithms and we need a way to compare multiple ways. Also, there are situations where we would like to know how much time and resources an algorithm might take when implemented. To measure performance of algorithms, we typically use time and space complexity analysis. The idea is to measure order of growths in terms of input size.

Independent of the machine and its configuration, on which the algorithm is running on.
Shows a direct correlation with the number of inputs.
Can distinguish two algorithms clearly without ambiguity.
Time Complexity: The time complexity of an algorithm quantifies the amount of time taken by an algorithm to run as a function of the length of the input. Note that the time to run is a function of the length of the input and not the actual execution time of the machine on which the algorithm is running on."""
# Python3 program for the above approach

# Function to find a pair in the given
# array whose sum is equal to z
def findPair(a, n, z) :
    
    # Iterate through all the pairs
    for i in range(n) :
        for j in range(n) :

            # Check if the sum of the pair
            # (a[i], a[j]) is equal to z
            if (i != j and a[i] + a[j] == z) :
                return True

    return False

# Driver Code

# Given Input
a = [ 1, -2, 1, 0, 5 ]
z = 0
n = len(a) 

# Function Call
if (findPair(a, n, z)) :
    print("True")
else :
    print("False")
    """Hence, the time complexity is O(N2) for the above algorithm. Note that the time complexity is solely based on the number of elements in array A i.e the input length, so if the length of the array will increase the time of execution will also increase."""
"""Space Complexity: 
Definition -

Problem-solving using computer requires memory to hold temporary data or final result while the program is in execution. The amount of memory required by the algorithm to solve given problem is called space complexity of the algorithm."""


"""Space Complexity: 
Definition -

Problem-solving using computer requires memory to hold temporary data or final result while the program is in execution.
The amount of memory required by the algorithm to solve given problem is called space complexity of the algorithm."""
"""(1) A fixed part: It is independent of the input size. It includes memory for instructions (code), constants, variables, etc.

(2) A variable part: It is dependent on the input size.
It includes memory for recursion stack, referenced variables, etc."""

"""Algorithm ADD SCALAR(A, B)
//Description: Perform arithmetic addition of two numbers
//Input: Two scalar variables A and B
//Output: variable C, which holds the addition of A and B
C <— A+B
return C"""
# Python program for the above approach

# Function to count frequencies of array items
def countFreq(arr, n):
    freq = dict()
    
    # Traverse through array elements and
    # count frequencies
    for i in arr:
        if i not in freq:
            freq[i] = 0
        freq[i]+=1
        
    # Traverse through map and print frequencies
    for x in freq:
        print(x, freq[x])

# Driver Code

# Given array
arr =  [10, 20, 20, 10, 10, 20, 5, 20 ]
n = len(arr)

# Function Call
countFreq(arr, n)

# This code is contributed by Shubham Singh