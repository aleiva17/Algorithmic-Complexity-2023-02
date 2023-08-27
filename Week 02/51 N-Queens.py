class Solution:
    def is_safe_place(self, grid: list[str], rows: int, y: int, x: int) -> bool:
        iterator = 1

        for index in range(y - 1, -1, -1):
            if grid[index][x] == "Q": return False
            if x - iterator >= 0 and grid[index][x - iterator] == "Q": return False
            if x + iterator < rows and grid[index][x + iterator] == "Q": return False
            iterator += 1

        return True

    def backtracking(self, answer_bank: list[list[str]], grid: list[list[str]], rows: int, current_row: int) -> None:
        # Si la fila en la que me encuentro es 1 después del máximo (porque cuento desde 0)
        # guardo el tablero que tengo hasta ahora en mi banco de respuestas
        if current_row == rows:
            # OJO: Guardamos una copia
            grid_copy = []

            for row in grid:
                copy_row = ""
                for col in row:
                    copy_row += col
                grid_copy.append(copy_row)

            answer_bank.append(grid_copy)
            return
        
        # Recorro cada una de las posibles posiciones en la fila actual.
        # Es decir, de 0 a n - 1
        for index in range(rows):
            # La celda actual es una posición válida para colocar una ficha
            # sin que las reinas se ataquen
            if self.is_safe_place(grid, rows, current_row, index):
                # Ubico temporalmente una reina
                grid[current_row][index] = "Q"

                # Llamo recursivamente para que resuelvan el problema en al siguiente fila
                self.backtracking(answer_bank, grid, rows, current_row + 1)

                # Revierto todos los cambios realizados
                for ind in range(rows):
                    grid[current_row][ind] = "."


    def solveNQueens(self, n: int) -> list[list[str]]:
        # Aquí almacenaremos todas las respuestas
        answer_bank = []
        
        # Creamos una matriz de tamaño n * n,. Cada celda
        # tiene un puntito.
        grid = [["." for _ in range(n)] for _ in range(n)]

        self.backtracking(answer_bank, grid, n, 0)

        return answer_bank


        