def is_safe(board,row,col,N):
    for i in range(row):
        if board[i] == col:
            return False
    
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i] == j:
            return False
    
    for i,j in zip(range(row,-1,-1),range(col,N)):
        if board[i] == j:
            return False
    return True

def solve_nqueen_util(board,row,N,solutions):
    if row>=N:
        solutions.append(board[:])
        return
    
    for col in range(N):
        if is_safe(board,row,col,N):
            board[row] = col
            solve_nqueen_util(board,row+1,N,solutions)


def solve_nqueen(N):
    board = [-1] *N
    solutions = []
    solve_nqueen_util(board,0,N,solutions)
    return solutions

def print_solutions(solutions,N):
    for sol in solutions:
        print("Solution : ")
        for i in range(N):
            row = ['.'] *N
            row[sol[i]] = 'Q'
            print(' '.join(row))
        print()

if __name__ =="__main__":
    N = int(input("Enter number of queens : "))
    solutions = solve_nqueen(N)
    print(f"Total Solutions are : {len(solutions)}")
    print_solutions(solutions,N)