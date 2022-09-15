#Rat in a maze Backtracking practice
#the maze is going to be a 5x5 matrix, 0 means a wall, 1 means a path the rat can go

import random
#initializing the maze
def init_maze(n):
    return [[0 for j in range(n)] for i in range(n)]
#function to shape an easy maze, here only by going right or down
def shape_maze(board, n):
    random.seed()
    board[0][0] = 1
    x, y = 0, 0
    while True:
        if x < n-1 and y < n-1:
            if random.randint(0, 1) == 1:
                x += 1
                board[x][y] = 1
            else:
                y += 1
                board[x][y] = 1
        elif x < n-1:
            x += 1
            board[x][y] = 1
        elif y < n-1:
            y += 1
            board[x][y] = 1
        elif x == n-1 and y == n-1:
            break
        else:
            break
    #this parts adds some dead ends to the maze
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                if random.randint(1,10) <= 3:
                    board[i][j] = 1
        
def printBoard(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
#check if the move can be done
def valid_move(board, n, move_x, move_y):
    if (move_x >= 0 and move_y >= 0 and move_x < n and move_y < n and board[move_x][move_y] == 1):
        return True
    return False
    
#main function, relies on rat_maze_util
def rat_maze(n, board):
    #intention to mark the used path with 2, changes shape of original board
    board[0][0] = 2
    #board is made in before the function runs
    #possible moves 
    move_x = [1,-1,0,0]
    move_y = [0,0,1,-1]

    if rat_maze_util(board, n, move_x, move_y, 0, 0):
        printBoard(board, n)
    else:
        print("No solution found")
        printBoard(board, n)
            
#backtracking function to solve the rat maze
    
def rat_maze_util(board, n, move_x, move_y, new_move_x, new_move_y):
    if new_move_x == n-1 and new_move_y == n-1:
        return True
    

    for i in range(4):
        new_move_x = new_move_x + move_x[i]
        new_move_y = new_move_y + move_y[i]
        if valid_move(board, n, new_move_x, new_move_y):
            board[new_move_x][new_move_y] = 2
            if rat_maze_util(board, n, move_x, move_y, new_move_x, new_move_y):
                return True
            board[new_move_x][new_move_y] = 0
    return False
    
    





if __name__ == "__main__":
    n = 5
    board = init_maze(n)
    shape_maze(board, n)
    printBoard(board, n)
    print()
    rat_maze(n, board)

