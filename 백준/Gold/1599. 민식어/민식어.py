import sys

input = sys.stdin.readline

lang = {'a':'a', 'b':'b', 'k':'c', 'd':'d', 'e':'e', 'g':'f'
    ,'h': 'g', 'i':'h', 'l':'i', 'm':'j', 'n':'k', 'ng':'l', 'o':'m'
           , 'p':'n', 'r':'o', 's':'p', 't':'q', 'u':'r', 'w':'s', 'y':'t'}

n = int(input())
s = []
for _ in range(n):
    string = input().rstrip()
    temp = ''
    flag = False
    i = 0
    while i < (len(string)):
        if i < len(string) - 1 and string[i] == 'n' and string[i+1] == 'g':
            i += 2
            temp += lang['ng']
            continue
        temp += lang[string[i]]
        i += 1
    s.append([temp, string])

s.sort(key=lambda x : x[0])

for i in s:
    print(i[1])