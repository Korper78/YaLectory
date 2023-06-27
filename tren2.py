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
#     dictry = sorted(file_in.readline().split())
#     text = file_in.readline().split()
#     for i in range(len(text)):
#         for word in dictry:
#             if text[i].startswith(word):
#                 text[i] = word
#                 break
#     # for word in dictry:
#     #     text = [word if w.startswith(word) else w for w in text]
#     print(*text, file=file_out)

# task D
# from collections import Counter
#
# with open('input.txt', 'r') as file_in, open('output.txt', 'w') as file_out:
#     n = int(file_in.readline())
#     arr = file_in.readline().split()
#     print(Counter(arr).most_common(1)[0][0], file=file_out)

# task C
from collections import Counter

with open('input.txt', 'r') as file_in, open('output.txt', 'w') as file_out:
    n = int(file_in.readline())
    arr = list(map(int, file_in.readline().split()))
    cnt = Counter(arr)
    cnt_keys = sorted(list(cnt.keys()))
    min_n = n - 2
    for k in range(len(cnt_keys) - 1):
        if cnt_keys[k+1] - cnt_keys[k] == 1:
            min_n = min(min_n, n - cnt[cnt_keys[k+1]] - cnt[cnt_keys[k+1]])
    print(min_n, file=file_out)
