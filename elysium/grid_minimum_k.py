

s = "aabaaaacaabc"
k = 2

def trim_middle(s):
    sorted_by_value = sorted(enumerate(s), key=lambda x: x[1])

    a, b, c = list(), list(), list()

    for index, letter in sorted_by_value:
        if letter == 'a':
            a.append((index, letter))
        if letter == 'b':
            b.append((index, letter))
        if letter == 'c':
            c.append((index, letter))

    compact = a[:k] + b[:k] + c[:k]

    left_side = list()
    right_side = list()

    middle_index = len(s) // 2

    for index in compact:
        if index < middle_index:
            left_side.append(index)

        else:
            right_side.append(index)
    
    list_s = list(s)

    return list_s[:max(left_side) + 1], list_s[min(right_side):][::-1]


def minimum_k(left: list, right: list, k: int, counter: dict = dict(), path_lengths: list = list(), last_added: str = str()):
    if not (left or right):
        counter[last_added] = counter.get(last_added, 0) - 1

        return
    
    if left:
        counter[left[0]] = counter.get(left[0], 0) + 1

        if counter.get('a', 0) >= k and counter.get('b', 0) >= k and counter.get('c', 0) >= k:
            path_lengths.append(sum(counter.values()))

        minimum_k(left[1:], right, k, counter, path_lengths, left[0])

    if right:
        counter[right[0]] = counter.get(right[0], 0) + 1

        if counter.get('a', 0) >= k and counter.get('b', 0) >= k and counter.get('c', 0) >= k:
            path_lengths.append(sum(counter.values()))

        minimum_k(left, right[1:], k, counter, path_lengths, right[0])

    counter[last_added] = counter.get(last_added, 0) - 1

    return 0 if not path_lengths else min(path_lengths)        


left, right = trim_middle(s)

print(minimum_k(left, right, k))