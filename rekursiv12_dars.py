# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)
# print(fact(5))
#
# def fibonachi(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonachi(n - 1) + fibonachi(n - 2)


# def fibonachi(n, cache={}):  # cache={2:1,4:3}
#     if n in cache:
#         return cache[n]
#     if n == 0:
#         result = 0
#     elif n == 1:
#         result = 1
#     else:
#         result = fibonachi(n - 1) + fibonachi(n - 2)
#     cache[n] = result
#     return result
#
#
# print(fibonachi(20))


def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        left = [x for x in lst[1:] if x <= pivot]
        right = [x for x in lst[1:] if x > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)


print(quick_sort([4, 6, 8, 9, 0, 1, 3, 4, 5, 6]))
