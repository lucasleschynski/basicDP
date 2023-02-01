
# Fills distance and "action" matrices through memoization. 
# Matrices used by generate_edit() to efficiently create lowest-cost edit.
# After running, d[last][last] stores Levenshtein distance.

def edit_dyn(s, t):
    d, a = generate_lists(s, t)
    
    for j in range(1, len(s)+1):
        for i in range(1, len(t)+1):
            if(s[j-1] == t[i-1]):
                d[j][i] = d[j-1][i-1]
                a[j][i] = 0
            else:
                d[j][i] = 1 + min(d[j][i-1], d[j-1][i], d[j-1][i-1])
                if(d[j][i] == d[j-1][i-1] + 1):
                    a[j][i] = 1
                elif(d[j][i] == d[j][i-1] + 1):
                    a[j][i] = 2
                elif(d[j][i] == d[j-1][i] + 1):
                    a[j][i] = 3
    return d, a

# Generates distance and "action" matrices for memoization functionality in edit_dyn()

def generate_lists(s, t):
    d = [[None]*(len(t) + 1) for i in range(0,len(s)+1)]
    a = [[None]*(len(t) + 1) for i in range(0,len(s)+1)]

    for i in range(0, len(t)+1):
        d[0][i] = i
        a[0][i] = 2

    for i in range(0, len(s)+1):
        d[i][0] = i
        a[i][0] = 3
    
    a[0][0] = 0 # Change a[0][0] to 0 manually, easier than adding case to array setup code.
    return d, a

# Uses action matrix to retrace most efficient edits, yielding an edit of word1 that most closely matches word2.

def generate_edit(word1, word2):
    a = edit_dyn(word1, word2)[1]
    b, c = [], []
    i, j = len(word1), len(word2)
    
    while i != 0 and j != 0:
        if(a[i][j] == 0 or a[i][j] == 1):
            b.append(word1[i-1])
            c.append(word2[j-1])
            i, j = i-1, j-1
        elif(a[i][j] == 2):
            b.append('-')
            c.append(word2[j-1])
            j -= 1
        elif(a[i][j] == 3):
            b.append(word1[i-1])
            c.append('-')
            i -= 1
    b = b[::-1]
    c = c[::-1]

    return b, c

print(generate_edit("ACCGGTATCCTAGGAC", "ACCTATCTTAGGAC"))