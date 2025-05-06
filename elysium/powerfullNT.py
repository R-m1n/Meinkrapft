
# ORIGINAL VERSION
def numberOfPowerfulInt(start, finish, limit, s):
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


# REVISED VERSION
def numberOfPowerfulInt(start: int, finish: int, limit: int, s: str) -> int:
    k = len(s)
    finish_str, start_str = str(finish), str(start)

    # Clamp a digit-string so all digits are less than or equal to `limit`
    def clamp(prefix, limit):
        for i, digit in enumerate(prefix):
            if int(digit) > limit:

                # Clamp this `digit` and pad the rest with `limit`
                return prefix[: i] + (str(limit) * (len(prefix) - i))

        return prefix

    # If `finish` has no room for any prefix, then the only candidate is either `s` itself or none.
    if len(finish_str) == k:
        return int(start <= int(s) <= finish)

    # Clamp finish_prefix which will represent our upper-bound in base(limit + 1)
    clamped_finish_prefix = clamp(finish_str[: -k], limit)

    # Count all prefixes up to the `clamped_finish_prefix`
    count = int(clamped_finish_prefix, base=limit + 1)

    # Include the upper-bound value if it still fits
    if int(clamped_finish_prefix + s) <= finish:
        count += 1

    if start > int(s):

        # If `start` is greater than `s` and `start` has no prefix, remove `s` itself
        if len(start_str) == k: 
            return count - 1

        # Clamp start_prefix which will represent our lower-bound in base(limit + 1)
        clamped_start_prefix = clamp(start_str[: -k], limit)

        # Remove prefixes that remain below `clamped_start_prefix`
        count -= int(clamped_start_prefix, base=limit + 1)

        # If by contactenating `clamped_start_prefix` and `s` the resulting number is less than `start`, remove it
        if int(clamped_start_prefix + s) < start:
            count -= 1

    return count