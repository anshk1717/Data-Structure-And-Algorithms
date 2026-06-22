"""
Problem:
Print a right-angled star triangle.

Input:
5

Output:
1
22
333
4444
55555

Time Complexity: O(n²)
Space Complexity: O(1)
"""

n = int(input("Enter a number: "))

for i in range(1, n+1):
    for j in range(1, i+1):
        print(i, end="")
    print()
