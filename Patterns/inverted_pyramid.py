"""
Problem:
Print an inverted full pyramid star pattern.

Input:
5

Output:
*********
 *******
  *****
   ***
    *

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

n = int(input("Enter a number: "))

for i in range(n):
    # spaces
    for j in range(i):
        print(" ", end="")

    # stars
    for j in range(2 * (n - i) - 1):
        print("*", end="")

    print()