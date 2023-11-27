# N queens problem using backtracking
# The N-Queens problem involves placing N chess queens on an N×N chessboard in such a way that no two queens threaten each other

N = int(input("Enter the number of queens: "))
board = [[0]*N for _ in range (N)]

def is_attack(i,j):
    #checks whether placing a queen at position (i, j) on the chessboard results in an attack
    for k in range(0,N):
        if board[i][k]==1 or board[k][j]==1:
            return True
    
    for k in range(0,N):
        for l in range(0,N):
            if(k+l == i+j) or (k-l == i-j):
                if board[k][l]==1:
                    return True
                
    return False


def n_queen(n):
    #uses backtracking to place queens one by one and checks for conflicts using the is_attack function
    if n==0: #n=0 means all queens are placed
        return True
    
    for i in range(0,N):
        for j in range(0,N):
            if(not(is_attack(i,j))) and (board[i][j]!=1):
                board[i][j]=1
                if n_queen(n - 1):
                    return True
                board[i][j]=0
    return False

n_queen(N)

for i in board:
    print(i)