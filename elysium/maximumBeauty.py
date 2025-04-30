items = [[1,2],[3,2],[2,4],[5,6],[3,5]]

queries = [6, 1, 2,3,4,5]

# price_to_max_beauty = dict()

# for price, beauty in items:
#     price_to_max_beauty[price] = max(price_to_max_beauty.get(price, 0), beauty)

# result = []

# prices = sorted(list(price_to_max_beauty.keys()))

# for query in queries:
#     max_beauty = 0

#     for price in prices:
#         if query < price:
#             break

#         max_beauty = max(price_to_max_beauty.get(price, 0), max_beauty)

#     result.append(max_beauty)

# items = sorted(items, key=lambda x: x[0])
# result = []

# for query in queries:
#     max_beauty = 0

#     for price, beauty in items:
#         if query < price:
#             break

#         max_beauty = max(beauty, max_beauty)

#     result.append(max_beauty)

# items = sorted(items, key=lambda x: x[0])
# price_to_max_beauty = list(dict(items).items())

# maxes = [0] * len(price_to_max_beauty)

# maxes[0] = price_to_max_beauty[0][1]
# for i in range(1, len(price_to_max_beauty)):
#     _, beauty = price_to_max_beauty[i]

#     maxes[i] = max(beauty, maxes[i - 1])

# print(maxes)

# print(price_to_max_beauty)

# items = [[1,1],[1,1000000000],[1,1000000000]]
# queries = [1000000000]

# items = sorted(items, key=lambda x: x[0])
# queries = sorted(queries)

# for i in range(1, len(items)):
#     _, current_beauty = items[i]
#     _, previous_beauty = items[i - 1]

#     items[i][1] = max(current_beauty, previous_beauty)

# price_to_max_beauty = dict(items)

# result = []

# max_beauty = 0

# for query in queries:
#     if query in price_to_max_beauty:
#         max_beauty = price_to_max_beauty.get(query)

#     result.append(max_beauty)

import bisect

items.sort()

for i in range(1, len(items)):
    items[i][1] = max(items[i][1], items[i-1][1])

prices = [price for price, _ in items]
max_beauties = [beauty for _, beauty in items]

result = []
for q in queries:
    index = bisect.bisect_right(prices, q) - 1

    if index >= 0:
        result.append(max_beauties[index])
    else:
        result.append(0)

print(result)
