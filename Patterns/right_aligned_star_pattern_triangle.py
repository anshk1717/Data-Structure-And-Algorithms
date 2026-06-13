"""
Problem:
Print a right-angled star triangle.

Input:
5

Output:
*
**
***
****
*****

Time Complexity: O(n²)
Space Complexity: O(1)
"""

n = int(input("Enter a number: "))

for i in range(n):
    for j in range(i + 1):
        print("*", end="")
    print()
