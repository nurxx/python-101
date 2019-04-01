word=input()
rows_and_columns=list(map(int,input().split()))

if len(word) > rows_and_columns[0] and len(word) > rows_and_columns[1]:
    print('Invalid input of rows or columns!')

matrix=[]
horizontal=[]
for i in range(rows_and_columns[0]):
    llist=list(map(str,input().split()))
    horizontal+=[''.join(llist)]
    matrix+=[llist]

vertical=[''.join([matrix[i][j] for i in range(rows_and_columns[0])]) for j in range(rows_and_columns[1])]

#Traversing diagonally - top left to bottom right
primary_diag_traverse=[]

# from top left to primary diagonal
for i in range(rows_and_columns[0]):
    string=''
    row = i 
    col = 0
    while row >= 0 and col < rows_and_columns[1] :
        string+=matrix[row][col]
        row -= 1
        col += 1
    primary_diag_traverse+=[string]

# from primary diagonal to bottom right
for i in range(1,rows_and_columns[1]):
    string=''
    row = rows_and_columns[0]-1 
    col = i
    while row >= 0 and col <rows_and_columns[1]:
        string+=matrix[row][col]
        row -= 1
        col += 1
    primary_diag_traverse+=[string]

#Traversing diagonally - top right to bottom left
secondary_diag_traverse=[]

# from top right to secondary diagonal
for i in range(rows_and_columns[0]):
    string=''
    row = i 
    col = rows_and_columns[1]-1
    while row >= 0 and col >= 0:
        string+=matrix[row][col]
        row -= 1
        col -= 1
    secondary_diag_traverse+=[string]

# from secondary diagonal to bottom left
for i in range(1,rows_and_columns[1]):
    string=''
    row = rows_and_columns[0]-1 
    col = rows_and_columns[1]- i-1 
    while row >= 0 and col >=0:
        string+=matrix[row][col]
        row -= 1
        col -= 1
    secondary_diag_traverse+=[string]

words=horizontal+vertical+primary_diag_traverse+secondary_diag_traverse

occurs=0
reversed_word=word[::-1]
for item in words:
    if word in item or reversed_word in item:
        occurs+=1

print(occurs) 




