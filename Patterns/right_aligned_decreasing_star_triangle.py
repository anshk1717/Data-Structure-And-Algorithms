"""
Problem:
Print a right-angled inverted star triangle.

Input:
5

Output:
*****
****
***
**
*

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

n = int(input("Enter a number: "))

for i in range(n):
    for j in range(n - i):
        print("*", end="")
    print()