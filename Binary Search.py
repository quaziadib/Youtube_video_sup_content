"""
Binary Search -----
    - Sorted Order Array or list
    - non-increasing function
    - non-decreasing function
"""


lst = [12, 15, 19, 25, 28, 32, 33, 48, 50]
#       0   1   2   3   4   5   6   7   8
#                               h   l

key = 34
# O(log N) "base of log is 2"
l = 0
h = len(lst) - 1  # 8

flag = 0

# loop
while l <= h:
    mid = (l + h) // 2
    # mid = l + (h - l)//2
    if lst[mid] == key:
        flag = 1
        print(f"Found match at {mid} index.")
        break
    elif lst[mid] > key:
        h = mid - 1
    else:
        l = mid + 1


if flag == 0:
    print("Not found!")
