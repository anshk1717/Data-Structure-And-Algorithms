"""
Problem:
Print a right-angled number triangle.

Input:
5

Output:
1
12
123
1234
12345

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()