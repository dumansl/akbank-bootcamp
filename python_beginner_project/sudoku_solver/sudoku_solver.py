def is_suitable(matrix,row,column, number_value):
    # step 1 
    for number in range(9):
        if matrix[row][number] == number_value:
            return False
    # step 2
    for number in range(9):
        if matrix[number][column] == number_value:
            return False
    # step 3
    new_row = row - row %3
    new_column = column - column %3
    for i in range(3):
        for j in range(3):
            if matrix[new_row + i][new_column + j] == number_value:
                return False
    return True

def solver(matrix,row =0 ,column = 0):
    if column == 9:
        row +=1
        column = 0
        if row == 9:
            return True
    if matrix[row][column] >0:
        return solver(matrix, row,column+1)
    for number_value in range(1,10):
        if is_suitable(matrix, row,column,number_value):
            matrix[row][column] = number_value

            if(solver(matrix, row,column+1)):
                return True
        matrix[row][column] =0
    return False

if __name__ == "__main__":
    sudoku = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    if solver(sudoku):
        for i in range(9):
            for j in range(9):
                print(sudoku[i][j], end=" ")
            print("")
    else:
        print("Bu sudoku yanlıştır, çözülemez")

# source : https://www.youtube.com/watch?v=065wtSUyQNU