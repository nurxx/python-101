def find_all_neighbours(i,j,matrix):
    neighbours=['matrix[i][j-1]','matrix[i][j+1]','matrix[i-1][j]','matrix[i+1][j]','matrix[i+1][j+1]','matrix[i-1][j-1]','matrix[i+1][j-1]','matrix[i-1][j+1]']
    row_indices=['i','i','i-1','i+1','i+1','i-1','i+1','i-1']
    col_indices=['j-1','j+1','j','j','j+1','j-1','j-1','j+1']
    damage=0
    for index,neighbour in enumerate(neighbours):
        try:
            exp=eval(neighbour)
            row=eval(row_indices[index])
            col=eval(col_indices[index])
            if exp < matrix[i][j] and row != -1 and col!=-1:
                damage += exp
            elif exp >= matrix[i][j] and row !=-1 and col !=-1:
                damage+= matrix[i][j]
        except Exception as e:
            pass

    return damage

def matrix_bombing_plan(m):
    sum_matrix=sum([m[i][j] for i in range (0,len(m)) for j in range(0,len(m[0]))])
    bombing={(i,j):(sum_matrix - find_all_neighbours(i,j,m))  for i in range(len(m)) for j in range(len(m[0]))}
    return bombing

def main():
    print(matrix_bombing_plan([[1,2,3],[4,5,6],[7,8,9]]))
    #print(matrix_bombing_plan([[10,10,10],[10,9,10],[10,10,10]]))

if __name__=='__main__':
    main()