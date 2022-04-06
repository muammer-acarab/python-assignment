text = input()
dict = {}

for i in text:
    dict[i] = text.count(i)

print(dict)

hello this is a test
{'h': 2, 'e': 2, 'l': 2, 'o': 1, ' ': 4, 't': 3, 'i': 2, 's': 3, 'a': 1}
​
"updated"
