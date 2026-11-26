# Time Complexity & Space Complexity

## 1. Introduction

In Data Structures and Algorithms (DSA), complexity analysis helps us evaluate how efficient an algorithm is.

There are two major types of complexity:

1. **Time Complexity:** Measures how the execution time of an algorithm grows as the input size increases.
2. **Space Complexity:** Measures how much additional memory an algorithm requires as the input size increases.

### Why Do We Need Complexity Analysis?

Consider two developers solving the same problem:

- Developer A writes an algorithm that takes 2 seconds for 1,000 elements.
- Developer B writes an algorithm that takes 0.1 seconds for 1,000 elements.

Developer B's algorithm is more efficient.

Complexity analysis helps us choose efficient algorithms, especially when working with large datasets.

---

## 2. Big-O Notation

Big-O notation describes the upper bound of an algorithm's growth rate.

It helps us understand how an algorithm performs when input size (n) increases.

### Common Time Complexities

| Complexity | Name | Example |
|---|---|---|
| O(1) | Constant | Array index access |
| O(log n) | Logarithmic | Binary Search |
| O(n) | Linear | Single loop |
| O(n log n) | Linearithmic | Merge Sort |
| O(n²) | Quadratic | Nested loops |
| O(n³) | Cubic | Three nested loops |
| O(2ⁿ) | Exponential | Recursive Fibonacci |
| O(n!) | Factorial | Generating all permutations |

### Complexity Growth Order

From most efficient to least efficient:

1. O(1)
2. O(log n)
3. O(n)
4. O(n log n)
5. O(n²)
6. O(n³)
7. O(2ⁿ)
8. O(n!)

---

## 3. Time Complexity with Python Examples

### A. O(1) – Constant Time

Execution time does not depend on input size.

```python
def get_first_element(arr):
    return arr[0]

print(get_first_element([10, 20, 30, 40]))
```

**Explanation:**
- Accesses only one element.
- Does not iterate through the array.
- Execution steps remain constant.

Real-life example: Finding the first contact in a list using its index.

### B. O(log n) – Logarithmic Time

The input size is reduced by a constant factor at every step.

```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1
```

**Explanation:**
- Each iteration eliminates approximately half of the search space.
- Requires a sorted array.
- Much faster than linear search for large sorted datasets.

Real-life example: Searching for a word in a dictionary by repeatedly dividing the pages into halves.

### C. O(n) – Linear Time

Execution time grows proportionally with input size.

```python
def print_elements(arr):
    for element in arr:
        print(element)
```

**Explanation:**
- One loop processes every element.
- If n = 100, approximately 100 iterations occur.
- If n = 1000, approximately 1000 iterations occur.

Real-life example: Checking every student in a class attendance list.

### D. O(n log n) – Linearithmic Time

Commonly found in efficient sorting algorithms.

```python
arr = [5, 2, 8, 1, 9]

arr.sort()
print(arr)
```

**Explanation:**
- Python's sorting algorithm uses Timsort.
- Its worst-case time complexity is O(n log n).

Real-life example: Sorting thousands of student records efficiently.

### E. O(n²) – Quadratic Time

Usually occurs when one loop is nested inside another loop.

```python
def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)
```

**Explanation:**
- Outer loop executes n times.
- Inner loop executes n times for every outer iteration.
- Total operations = n × n = n².

Real-life example: Comparing every student with every other student.

### F. O(2ⁿ) – Exponential Time

The number of operations approximately doubles with each additional input element.

```python
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)
```

**Explanation:**
- Each function call generates two recursive calls (except base cases).
- The number of calls grows exponentially.
- This is an inefficient approach for large n.

Real-life example: Exploring all possible combinations of choices.

---

## 4. Space Complexity

Space complexity measures the memory required by an algorithm.

It includes auxiliary space (extra memory used by the algorithm) and, depending on the definition, input storage.

### A. O(1) – Constant Space

```python
def calculate_sum(a, b):
    result = a + b
    return result
```

**Explanation:**
- Uses a fixed number of variables.
- Memory usage does not grow with input size.

### B. O(n) – Linear Space

```python
def create_list(n):
    result = []

    for i in range(n):
        result.append(i)

    return result
```

**Explanation:**
- Creates a new list.
- Stores n elements.
- Memory grows linearly with input size.

### C. O(n) – Recursive Space

```python
def countdown(n):
    if n == 0:
        return

    countdown(n - 1)
```

**Explanation:**
- Each recursive call occupies a stack frame.
- Maximum recursion depth is n.
- Auxiliary space complexity is O(n).

### D. O(n²) – Quadratic Space

```python
def create_matrix(n):
    matrix = []

    for i in range(n):
        row = [0] * n
        matrix.append(row)

    return matrix
```

**Explanation:**
- Creates an n × n matrix.
- Stores n² elements.
- Space complexity is O(n²).

---

## 5. Time Complexity vs Space Complexity

| Time Complexity | Space Complexity |
|---|---|
| Measures execution growth | Measures memory growth |
| Focuses on operations | Focuses on memory allocation |
| Helps optimize speed | Helps optimize memory |
| Example: Binary Search O(log n) | Example: Recursive Countdown O(n) |

### Time-Space Tradeoff

Sometimes we use additional memory to improve execution speed.

Example:

**Without Hash Set:**

```python
def contains_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True

    return False
```

Time Complexity: O(n²)  
Auxiliary Space Complexity: O(1)

**With Hash Set:**

```python
def contains_duplicate(arr):
    seen = set()

    for num in arr:
        if num in seen:
            return True

        seen.add(num)

    return False
```

Average Time Complexity: O(n)  
Auxiliary Space Complexity: O(n)

**Conclusion:** We use extra memory to improve execution speed.

---

## 6. Important Rules for Calculating Complexity

### Rule 1: Ignore Constants

```python
for i in range(n):
    print(i)

for j in range(n):
    print(j)
```

Complexity: O(2n) → O(n)

### Rule 2: Keep the Highest Order

```python
for i in range(n):
    print(i)

for i in range(n):
    for j in range(n):
        print(i, j)
```

Complexity: O(n + n²) → O(n²)

### Rule 3: Nested Loops Multiply

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

Complexity: O(n × n) = O(n²)

### Rule 4: Sequential Loops Add

```python
for i in range(n):
    print(i)

for j in range(n):
    print(j)
```

Complexity: O(n + n) = O(n)

### Rule 5: Different Input Sizes

```python
def example(a, b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)
```

Complexity: O(a + b), not O(n).

---

## 7. Best, Average and Worst Case

| Case | Meaning |
|---|---|
| Best Case | Minimum operations |
| Average Case | Expected operations |
| Worst Case | Maximum operations |

Example: Linear Search

```python
def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1
```

- Best Case: O(1) – Target is the first element.
- Average Case: O(n) – Target is somewhere in the middle.
- Worst Case: O(n) – Target is the last element or not present.

---

## 8. Common Data Structure Operations

| Operation | Average Time Complexity |
|---|---|
| Array/List Index Access | O(1) |
| List Search | O(n) |
| List Append | O(1) amortized |
| List Insert at Beginning | O(n) |
| Dictionary Lookup | O(1) |
| Set Lookup | O(1) |
| Stack Push | O(1) |
| Stack Pop | O(1) |
| Queue Enqueue (Deque) | O(1) |
| Queue Dequeue (Deque) | O(1) |

Note: Dictionary and set operations have O(n) worst-case complexity.

---

## 9. Interview Preparation – Important Questions

1. What is time complexity?
2. What is space complexity?
3. What is Big-O notation?
4. Difference between O(1) and O(n)?
5. Why is binary search O(log n)?
6. Why do nested loops generally result in O(n²)?
7. What is auxiliary space?
8. What is the time-space tradeoff?
9. Difference between best, average and worst case?
10. Why do we ignore constants in Big-O?
11. What is recursion stack space?
12. Why is hash table lookup O(1) on average?
13. What is the complexity of merge sort?
14. What is the difference between O(n) and O(n log n)?
15. Can an algorithm have O(n) time and O(1) auxiliary space?

---

## 10. Practice Tasks

Try calculating the time and auxiliary space complexity of each function.

### Problem 1

```python
def example1(n):
    for i in range(n):
        print(i)
```

### Problem 2

```python
def example2(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
```

### Problem 3

```python
def example3(n):
    i = 1

    while i < n:
        i *= 2
```

### Problem 4

```python
def example4(n):
    result = []

    for i in range(n):
        result.append(i)

    return result
```

### Problem 5

```python
def example5(n):
    if n <= 1:
        return

    example5(n - 1)
```

---

## 11. Key Takeaways

- Time Complexity measures algorithm execution growth.
- Space Complexity measures memory growth.
- Big-O describes an asymptotic upper bound.
- O(1) is constant complexity.
- O(log n) is logarithmic complexity.
- O(n) is linear complexity.
- O(n²) is quadratic complexity.
- Nested loops often multiply complexity.
- Sequential loops generally add complexity.
- Efficient algorithms balance time and memory.

**Learning Goal:** Be able to analyze any basic Python function, calculate its time and auxiliary space complexity, and explain your reasoning in a software engineering interview.

**Next Step:** Practice complexity analysis alongside Striver's A2Z DSA Sheet.