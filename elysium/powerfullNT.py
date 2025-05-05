

def distill(number: str, limit: int):
    bound = ""
    residue = 0

    for i in range(len(number)):
        if int(number[i]) > limit:
            bound += str(limit)

            residue += len(number) - i - 1
            
            break

        bound += number[i]

    return bound + (str(limit) * residue)


def to_decimal(number: str, base: int):
    decimal = 0

    power = 0
    for digit in number[::-1]:
        decimal += pow(base, power) * int(digit)

        power += 1

    return decimal

def numberOfPowerfulInt(start, finish, limit, s):
    str_finish, str_start = str(finish), str(start)

    upper_positions = len(str_finish) - len(s)

    if upper_positions == 0:
        return int(start <= int(s) <= finish)

    upper_bound = distill(str_finish[: upper_positions], limit)

    result = to_decimal(upper_bound, limit + 1)

    if int(upper_bound + s) <= finish:
        result += 1

    if start > int(s):
        lower_positions = len(str_start) - len(s)

        if lower_positions == 0:
            return result - 1

        lower_bound = distill(str_start[:lower_positions], limit)

        result -= to_decimal(lower_bound, limit + 1)

        if int(lower_bound + s) < start:
            result -= 1

    return result


