
Python DSA – Problem-Solving Fundamentals
Based on TakeUForward learning topics | 22 November 2026
1. Flowchart
A flowchart is a graphical representation of an algorithm. It shows the sequence of steps required to solve a problem.
Common flowchart symbols
Symbol	Meaning	Example
Oval	Start / End	Start
Rectangle	Process	sum = a + b
Parallelogram	Input / Output	Input n
Diamond	Decision	n > 0?
Arrow	Flow direction	Next step

Real-life example
Imagine withdrawing money from an ATM:
1. Start.
2. Insert ATM card.
3. Enter PIN.
4. Check whether PIN is correct.
5. If correct, enter withdrawal amount.
6. Check available balance.
7. Dispense cash.
8. End.
This is the same decision-making logic we use in programming.
Programming example
Problem: Check whether a number is positive or negative.
n = int(input("Enter number: "))if n > 0:    print("Positive")elif n < 0:    print("Negative")else:    print("Zero")




2. Pseudocode
Pseudocode is a simple, human-readable way to describe the logic of a program without following the exact syntax of a programming language.

It helps you plan the solution before writing Python code.
Example: Find the sum of two numbers
Pseudocode:
START

INPUT a
INPUT b

sum = a + b

PRINT sum

END


Python implementation:
a = 10b = 20total = a + bprint(total)



Output:
30


Common pseudocode keywords
Keyword	Purpose
START	Begin algorithm
INPUT	Receive input
OUTPUT	Display result
SET	Assign a value
IF	Check condition
ELSE	Alternative condition
WHILE	Repeat while condition is true
FOR	Repeat a fixed number of times
RETURN	Return a result
END	Finish algorithm


3. Dry Run
A dry run means executing code manually, step by step, without actually running the program.

It helps you understand how variables change during execution.
Example: Sum of numbers from 1 to N
n = 5total = 0for i in range(1, n + 1):    total = total + iprint(total)



Output:
15


Dry-run table
Iteration	i	total before	total after
1	1	0	1
2	2	1	3
3	3	3	6
4	4	6	10
5	5	10	15

Important: Always track the values of variables, loop conditions and output.

4. Edge Cases
An edge case is a special or boundary input that might expose a problem in your code.

For example, suppose you write a function that finds the largest number in a list.
def largest(arr):    return max(arr)



Test these cases:
Input	Expected output
[1, 2, 3]	3
[5]	5
[-5, -2, -10]	-2
[7, 7, 7]	7
[0, 0, 0]	0
[]	Requires special handling

Important types of edge cases
1. Minimum input.
2. Maximum input.
3. Empty input.
4. Single-element input.
5. Negative numbers.
6. Duplicate elements.
7. Already sorted elements.
8. Reverse-sorted elements.
9. Zero.
10. Boundary values.
Real-life example: A banking application should not allow a withdrawal greater than the available balance. Testing a withdrawal equal to the balance and one rupee above it checks the boundary.

5. Debugging
Debugging is the process of identifying, understanding and fixing errors in a program.
Three major types of errors
A. Syntax error

Incorrect Python syntax.
if n > 5    print("Greater")



Missing colon.

Correct:
if n > 5:    print("Greater")



B. Runtime error

An error that occurs while the program is executing.
a = 10b = 0print(a / b)



Output:
ZeroDivisionError


C. Logical error

The program executes but produces an incorrect result.
for i in range(1, 5):    print(i)



If you want numbers from 1 to 5, this code is incorrect because range() excludes the ending value.

Correct:
for i in range(1, 6):    print(i)



Debugging techniques
- Use print() to inspect variables.
- Use breakpoints in VS Code.
- Read error messages and tracebacks.
- Check loop boundaries.
- Perform a manual dry run.
- Test different inputs.
Debugging workflow