text = "the quick brown fox jumps over the lazy dog"

text2 = text.split("u")
text2len = 0
for i in range(len(text2)):
    text2len += len(text2[i])
print(len(text)-text2len)

count = 0
for char in text:
    if char == "u":
        count = count+1
print(count)

s = "my name is samuel lopez"
letter_dict = {}
for char in s:
    if char not in letter_dict.keys():
        letter_dict[char] = 1
    else:
        letter_dict[char] = letter_dict[char] + 1
print(letter_dict)