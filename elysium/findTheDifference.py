from collections import Counter
s = "ae"
t = "aea"

larger = Counter(s) if len(s) > len(t) else Counter(t) 
smaller = Counter(s) if len(s) <= len(t) else Counter(t)

print((larger - smaller).popitem()[0])

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        larger = s if len(s) > len(t) else t
        smaller = s if len(s) <= len(t) else t

        larger_ascii_total = 0
        for letter in larger:
            larger_ascii_total += ord(letter)

        smaller_ascii_total = 0
        for letter in smaller:
            smaller_ascii_total += ord(letter)

        for ascii in range(ord('a'), ord('z') + 1):
            if smaller_ascii_total + ascii == larger_ascii_total:
                return chr(ascii)
