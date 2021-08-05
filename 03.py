str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

str1 = str.replace(',', '')
str2 = str1.replace('.', '')

list = str2.split()

ans = [len(i) for i in list]

print(ans)