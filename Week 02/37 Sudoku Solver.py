# [BACKTRACKING] PROBLEM LINK: https://leetcode.com/problems/sudoku-solver/description/ 

class Solution:
    def is_valid_number_on_position(self, number: int, x: int, y: int, board: list[list[str]]) -> bool:
        # Convertimos el int a string porque el board lo guardaa como str
        number = str(number)
        
        # Revisamos si se repite el número en la misma columna y/o fila
        for index in range(9):
            if board[y][index] == number or board[index][x] == number:
                return False
        
        # Revisamos que el número no se repita en el mismo subcuadrado
        start_sub_square_x = x - x % 3
        start_sub_square_y = y - y % 3

        for row in range(3):
            for col in range(3):
                if board[start_sub_square_y + row][start_sub_square_x + col] == number:
                    return False 

        # Podemos colocar el numero en la presente coordenada
        return True

    def backtracking(self, x: int, y: int, board: list[list[str]]) -> bool:
        # Si estamos revisando la columna x == 9, significa que ya terminamos
        # de revisar esa fila. Porque van de 0 a 8. Por lo tanto, tenemos que
        # continuar desde el inicio de la siguiente fila
        if x == 9: 
            return self.backtracking(0, y + 1, board)
        
        # Si estamos revisando la fila y == 9, significa que ya terminamos de revisar
        # la última fila del sudoku. Por lo tanto, retornamos True porque ya hemos.
        # hallado una solución al sudoku.
        if y == 9: 
            return True

        # Si la celda que me toca revisar ya tiene asignado un número, debo continuar
        # con la siguiente celda
        if board[y][x] != ".": 
            return self.backtracking(x + 1, y, board)

        # Estoy en una celda vacía donde debo colocar un número del 1 al 9. Por lo tanto,
        # debo explorar esas soluciones.
        for digit in range(1, 10):
            # Si no puedo colocar este dígito en esta celda, continúo con el siguiente número
            if not self.is_valid_number_on_position(digit, x, y, board):
                continue
            
            # Coloco temporalmente el número en la presente celda
            board[y][x] = str(digit)

            # Exploro recursivamente si se encuentra una solución con este número en esta celda para el resto
            # de celdas. Para eso, voy en orden aumentando el x + 1.
            if self.backtracking(x + 1, y, board):
                return True

            # Como no encontró recursivamente un solución, debo revertir los cambios realizados previamente
            board[y][x] = "."
        
        # Si llegué aquí, significa que no pude colocar un número válido del 1 al 9 en la presente celda
        # Por lo tanto, retorno False
        return False


    def solveSudoku(self, board: list[list[str]]) -> None:
        # Empiezo a llenar el tablero desde la fila superior izquierda (0, 0) 
        # hasta la inferior derecha (8, 8).
        self.backtracking(0, 0, board)