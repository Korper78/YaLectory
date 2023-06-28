# task A
# with open('input.txt', 'r') as file_in, open('output.txt', 'w') as file_out:
#     n = int(file_in.readline())
#     arr = [0]
#     for num in map(int, file_in.readline().split()):
#         arr.append(arr[-1] + (num > 0))
#     q = int(file_in.readline())
#     for _ in range(q):
#         l, r = map(int, file_in.readline().split())
#         print(arr[r] - arr[l-1], file=file_out)

# task B
# with open('input.txt', 'r') as file_in, open('output.txt', 'w') as file_out:
#     n = int(file_in.readline())
#     arr = sorted(list(map(int, file_in.readline().split())))
#     l, r, c = 0, 1, 0
#     while l < n - 1:
#         if arr[r] < (arr[l] * 2 - 14):
#             c += 1 + (arr[l] == arr[r])
#             if r < n - 1:
#                 r += 1
#             else:
#                 l += 1
#         else:
#             l += 1
#             r += r == l
#     print(c, file=file_out)

# task C
