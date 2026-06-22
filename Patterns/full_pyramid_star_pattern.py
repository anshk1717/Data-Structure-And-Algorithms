"""
Problem:
Print a full pyramid star pattern.

Input:
5

Output:
    *
   ***
  *****
 *******
*********

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

n = int(input("Enter a number: "))

for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(2*i+1):
        print("*", end="")
    print()
