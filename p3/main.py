def lcs(word1, word2):
    len1 = len(word1)
    len2 = len(word2)
    grid = [[0 for j in range(len2+1)] for i in range(len1+1)]
    count = 0
    for i in range(1,(len1+1)):
        for j in range(1,(len2+1)):
            if word1[i-1] == word2[j-1]:
                grid[i][j] = grid[i-1][j-1] + 1
            else:
                grid[i][j] = max(grid[i-1][j], grid[i][j-1])
    return grid[-1][-1]
    
def suggestion(query, word1, word2):
    first = lcs(query, word1)
    second = lcs(query, word2)
    if first >= second:
        sugg =  word1
    else: sugg = word2
    return sugg
    
f = open('INPUT.txt', 'r')
text = f.readlines()
words = []
for entry in text:
    if entry != '\n':
        words.append(entry.strip())
num = words.pop(0)
num = int(num)
ans = []
for i in range(num):
    query = words.pop(0)
    word1 = words.pop(0)
    word2 = words.pop(0)
    ans.append(suggestion(query,word1,word2))
with open('OUTPUT.txt', 'w') as f:
    for word in ans:
        f.write(word+ '\n')



