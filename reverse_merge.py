def merge(left, right, lst):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            lst[k] = left[i]
            i = i + 1
        else:
            lst[k] = right[j]
            j = j + 1

        k = k + 1

    while i < len(left):
        lst[k] = left[i]
        i = i + 1
        k = k + 1

    while j < len(right):
        lst[k] = right[j]
        j = j + 1
        k = k + 1

def merge_sort(lst):
    if len(lst) < 2:
        return lst

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    merge_sort(left)
    merge_sort(right)

    merge(left, right, lst)

lst = [3, 5, 1, 2, 6, 7, 9, 8, 4, 5]
merge_sort(lst)
print("test 1",lst)
assert lst == [9, 8, 7, 6, 5, 5, 4, 3, 2, 1]

lst = [10, 8, 9, 15, 7, 6, 5, 2, 3]
merge_sort(lst)
print("test 2",lst)
assert lst == [15, 10, 9, 8, 7, 6, 5, 3, 2]

lst = [10, 8, 9, 15, 7, 6, 5]
merge_sort(lst)
print("test 3", lst)
assert lst == [15, 10, 9, 8, 7, 6, 5]

lst = [10, 8, 9, 15]
merge_sort(lst)
print("test 4",lst)
assert lst == [15, 10, 9, 8]

lst = [3, 5, 1, 2, 6]
merge_sort(lst)
print("test 5",lst)
assert lst == [6, 5, 3, 2, 1]