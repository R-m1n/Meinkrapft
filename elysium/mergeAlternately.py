word1 = "ab"
word2 = "pqrs"

larger_len = len(word2) if len(word2) > len(word1) else len(word1)

output = ['' for _ in range(2 * larger_len)]

for i in range(len(word1)):
    output[2*i] = word1[i]

for i in range(len(word2)):
    output[2*i+1] = word2[i]

print(''.join(output))

#########

output = ''

if len(word2) > len(word1):
    for i in range(len(word2)):
        if i < len(word1):
            output += word1[i]

        output += word2[i]
else:
    for i in range(len(word1)):
        output += word1[i]

        if i < len(word2):
            output += word2[i]