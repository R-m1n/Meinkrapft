import string


def lengthOfLongestSubstring(s: str) -> int:
    def is_unique(slice):
        uniques = set()

        for char in slice:
            if char in uniques:
                return False
        
            uniques.add(char)

        return True

    printable = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + " "
    if len(s) == 1:
        return 1

    if printable in s:
        return len(printable)

    for sliding_window in range(len(s), 0, -1):
        for i in range(len(s) - sliding_window + 1):
            slice = s[i: i + sliding_window]
            if is_unique(slice):
                return len(slice)
        
    return 0

