# task A
# import math
#
# n = int(input())
# print(int((math.sqrt(n * 8 + 1) - 1) // 2))

# task B
# u_str = list(filter(lambda subs: subs and subs != '.', input().strip('/').split('/')))
# c_str = []
# for d in u_str:
#     if d != '..':
#         c_str.append(d)
#     else:
#         if c_str:
#             c_str.pop()
# print('/' + '/'.join(c_str))

# task C
with open('input.txt', 'r') as file_in, open('output.txt', 'w') as file_out:
    n = int(file_in.readline())
    prices = list(map(int, file_in.readline().split()))
    day_min, day_max, min_day = 0, 0, 0
    for day in range(1, n):
        if prices[day_max] * prices[min_day] < prices[day_min] * prices[day]:
            day_min, day_max = min_day, day
        if prices[day] < prices[min_day]:
            min_day = day
    if day_max:
        print(f'{day_min+1} {day_max+1}', file=file_out)
    else:
        print('0 0', file=file_out)

# task D
# from time import strptime
#
# with open('input.txt', 'r') as file_in, open('output.txt', 'w') as file_out:
#     n = int(file_in.readline())
#     times = sorted(strptime(time, '%H:%M').tm_hour * 60 + strptime(time, '%H:%M').tm_min for time in file_in.readline().split())
#     min_interval = 24 * 60
#     for i in range(len(times)):
#         j = (i + 1) % len(times)
#         diff = times[j] - times[i] if times[j] >= times[i] else times[j] - times[i] + 24 * 60
#         min_interval = min_interval if min_interval < diff else diff
#     print(min_interval, file=file_out)

# task E
# import re
#
# palindrome = input()
# not_a = re.search('[b-z]', palindrome)
# not_palindrome = ''
# # if not_a and not_a.start() != len(palindrome) // 2:
# if not_a:
#     if not_a.start() == len(palindrome) // 2:
#         if palindrome[not_a.start()] == 'b':
#             not_palindrome = palindrome[:not_a.end()] + 'b' + palindrome[not_a.end()+1:]
#         else:
#             not_palindrome = palindrome[:not_a.start()] + 'b' + palindrome[not_a.end():]
#     else:
#         not_palindrome = palindrome[:not_a.start()] + 'a' + palindrome[not_a.end():]
# elif len(palindrome) > 1:
#     not_palindrome = palindrome[:-1] + 'b'
#     # not_palindrome = palindrome[:not_a.start()] + 'a' + palindrome[not_a.end():]
# print(not_palindrome)
