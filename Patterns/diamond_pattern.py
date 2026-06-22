"""
Problem:
Print a diamond star pattern.

Input:
5

Output:
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *

Approach:
1. Print the upper half (full pyramid).
2. Print the lower half (inverted pyramid).
3. Skip the first row of the lower half to avoid printing the middle row twice.

Time Complexity: O(n²)
Space Complexity: O(1)
"""

n = int(input("Enter a number: "))

# Upper Half
for i in range(n):
    spaces = n - i - 1
    stars = 2 * i + 1

    print(" " * spaces + "*" * stars)

# Lower Half
for i in range(1, n):
    spaces = i
    stars = 2 * (n - i) - 1

    print(" " * spaces + "*" * stars)