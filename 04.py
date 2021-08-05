str = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

str1 = str.replace(',', '')
str2 = str1.replace('.', '')
list = str2.split()
numlist = [1, 5, 6, 7, 8, 9, 15, 16, 19]
ans = {}

for i, key in enumerate(list):
    if i + 1 in numlist:
        ans[key[:1]] = i + 1
    else:
        ans[key[:2]] = i + 1

print(ans)
