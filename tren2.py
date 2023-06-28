# task A
# with open('input.txt', 'r') as file_in, open('output.txt', 'w') as file_out:
#     n, k = list(map(int, file_in.readline().split()))
#     # values = list(map(int, file_in.readline().split()))
#     values = file_in.readline().split()
#     answer = 'NO'
#     # for i in range(k, n):
#     #     if len(set(values[i-k:i+1])) < k + 1:
#     #         answer = 'YES'
#     #         break
#     for i in range(n - k):
#         if values[i] in values[i+1:i+k+1]:
#             answer = 'YES'
#             break
#     print(answer, file=file_out)

# task B
# from collections import defaultdict
#
# s = input()
# sticks = defaultdict(set)
# for i in range(1, len(s), 2):
#     sticks[s[i]].add(s[i-1])
# print(sum([1 for v in sticks.values() if len(v) == 3]))

# task C
# with open('input.txt', 'r') as file_in, open('output.txt', 'w') as file_out:
#     dictry = set(file_in.readline().split())
#     text = file_in.readline().split()
#     for i in range(len(text)):
#         for j in range(1, min(101, len(text[i]))):
#             if text[i][:j] in dictry:
#                 text[i] = text[i][:j]
#                 break
#     print(*text, file=file_out)

# task D
# from collections import Counter
#
# with open('input.txt', 'r') as file_in, open('output.txt', 'w') as file_out:
#     n = int(file_in.readline())
#     arr = file_in.readline().split()
#     print(Counter(arr).most_common(1)[0][0], file=file_out)

# task E
from collections import Counter

with open('input.txt', 'r') as file_in, open('output.txt', 'w') as file_out:
    n = int(file_in.readline())
    arr = list(map(int, file_in.readline().split()))
    cnt = Counter(arr)
    max_n = 0
    for k in cnt.keys():
        max_n = max(max_n, cnt[k] + cnt.get(k+1, 0), cnt[k] + cnt.get(k-1, 0))
    print(n - max_n, file=file_out)
