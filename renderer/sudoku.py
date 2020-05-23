#Sudoku


# board = [
#         [7, 8, 0,  4, 0, 0,  1, 2, 0],
#         [6, 0, 0,  0, 7, 5,  0, 0, 9],
#         [0, 0, 0,  6, 0, 1,  0, 7, 8],
#         #line -------------
#         [0, 0, 7,  0, 4, 0,  2, 6, 0],
#         [0, 0, 1,  0, 5, 0,  9, 3, 0],
#         [9, 0, 4,  0, 6, 0,  0, 0, 5],
#         #line -------------
#         [0, 7, 0,  3, 0, 0,  0, 1, 2],
#         [1, 2, 0,  0, 0, 7,  4, 0, 0],
#         [0, 4, 9,  2, 0, 6,  0, 0, 7]
#         ]

def algos(bor):
    #Backtrack Algo to solve the board 
    find = empty_find(bor)
    
    if not find:
        return True
    else:
        row, col = find
    
    for i in range(1,10):
        
        if find_valid(bor, i,(row,col)):
            bor[row][col] = i

            if algos(bor):
                return True

            bor[row][col]=0
    
    return False



def find_valid(bor, num, position):
    #checking row for getting same num exists or not
    for i in range(len(bor)):
        if bor[position[0]][i] == num and position[1] != i:
            return False
    #checking column for the same
    for  i in range(len(bor)):
        if bor[i][position[1]] == num and position[0] != i:
            return False 
    
    #checking Boxes if that number exists or not already
    box_column = position[1] // 3 
    box_row = position[0] // 3

    for i in range(box_row*3,box_row*3+3):
        for j in range(box_column*3,box_column*3+3):
            if bor[i][j]==num and (i,j) != position:
                return False
    return True



def print_board(bor):
    for i in range(len(bor)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bor[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bor[i][j])
            else:
                print(str(bor[i][j]) + " ", end="")

def empty_find(bo):
    # print(len(bor))
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None


def start(board):
    algos(board)
    solved = {}
    solved["board"]=board
    return solved