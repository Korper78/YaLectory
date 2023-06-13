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
    day_min, day_max, diff = 0, 0, 0
    for day in range(1, n):
        # price = prices.pop(0)
        price = prices[day - 1]
        # gt_price = max(prices, key=lambda p: p-price)
        gt_price = max(prices[day:])
        # profit = 1000 / price * gt_price - 1000
        profit = gt_price / price - 1
        if profit > diff:
            # day_min, day_max, diff = day, day + prices.index(gt_price) + 1, profit
            day_min, day_max, diff = day, day + prices[day:].index(gt_price) + 1, profit
    print(f'{day_min} {day_max}', file=file_out)
