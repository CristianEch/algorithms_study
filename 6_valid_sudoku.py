class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        state = True
        fila = 0
        boxes = {(0,0):[], (1,0):[], (2,0):[], (0,1):[], (1,1):[], (2,1):[], (0,2):[], (1,2):[], (2,2):[]}
        columns = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}
        filas = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}
        
        for row in board:
            columna = 0
            
            for element in row:
                x = columna//3
                y = fila//3
                
                if ord(element)>= 49 and ord(element)<=57:
                    if element not in boxes[(x,y)]:
                        boxes[(x,y)].append(element)
                    else:
                        #print(f"-------------------{element} is repeated------------------------")
                        state = False
                    if element not in columns[columna]:
                        columns[columna].append(element)
                    else:
                        #print(f"-------------------{element} is repeated------------------------")
                        state = False
                    if element not in filas[fila]:
                        filas[fila].append(element)
                    else:
                        #print(f"-------------------{element} is repeated------------------------")
                        state = False
                columna += 1
            fila +=1
        return state

            
                        
sudoku_1 = [["5","3",".",".","7",".",".","2","1"],
            ["6",".",".","1","9","5",".","6","4"],
            ["3","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            ["$",".",".",".","8",".",".","7","9"]]    


sol = Solution()

print(sol.isValidSudoku(sudoku_1))