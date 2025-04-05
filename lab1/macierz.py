from typing import List, Union, Tuple
import numpy as np

class Macierz:
    def __init__(self, matrix: Union[List[List[Union[int, float]]], Tuple[int, int]], val: Union[int, float] = 0):
        if not isinstance(val, (int, float)):
            raise ValueError('Błędne dane wejściowe')
        
        if isinstance(matrix, list):
            self.__matrix = matrix
        elif isinstance(matrix, tuple):
            self.__matrix = [[val for col in range(matrix[1])] for row in range(matrix[0])]
        else:
            raise ValueError('Błędne dane wejściowe')
            
        
    def __add__(self, other: "Macierz") -> "Macierz":
        if not isinstance(other, Macierz):
            raise ValueError('Nie można dodawać do siebie obiektów różnych typów')
        if self.size()[0] != other.size()[0] or self.size()[1] != other.size()[1]:
            raise ValueError('Nie można dodawać dwóch macierzy o różnych rozmiarach')
        
        mat: Macierz = Macierz([[self.__matrix[row][col] + other[row][col] for col in range(len(self.__matrix[0]))] for row in range(len(self.__matrix))])
        return mat
        

    def __mul__(self, other: "Macierz") -> "Macierz":
        rst: Macierz = Macierz((self.size()[0], other.size()[1]))
        if self.size()[0] != other.size()[1]:
            raise ValueError('Nie można pomnożyć takich dwóch macierzy')
        for row_1 in range(self.size()[0]):
            for col_2 in range(other.size()[1]):
                for n in range(self.size()[1]):
                    rst[row_1][col_2] += self.__matrix[row_1][n] * other[n][col_2]

        return rst

        
    def __getitem__(self, row: int) -> List[Union[int, float]]:
        if not isinstance(row, int):
            raise TypeError('Indeksy listy muszą być typu int')
        return self.__matrix[row]
    
    def __str__(self) -> str:
        wth: int = max(len(str(self.__matrix[row][col])) for row in range(self.size()[0]) for col in range(self.size()[1]))+1
        rst: str = ''
        for row in range(self.size()[0]):
            rst += "|"
            for col in range(self.size()[1]):
                rst += f"{self.__matrix[row][col]:>{wth}}"
            rst += " |\n"

        return rst
            
    def size(self) -> Tuple[int, int]:
        rows_n: int = len(self.__matrix)
        cols_n: int = len(self.__matrix[0])

        return rows_n, cols_n
    

def mat_transp(mat: "Macierz"):
    nrow, ncol = mat.size()
    matrix: "Macierz" = Macierz((ncol, nrow))
    for nr in range(nrow):
        for nc in range(ncol):
            matrix[nc][nr] = mat[nr][nc]
                
    return matrix


def Chio(old_matrix: Macierz, val:float = 1.) -> int | float:

    if old_matrix[0][0] == 0:
        s = old_matrix.size()
        acc_row: int 
        for n_row in range(s[0]):
            if old_matrix[n_row][0] != 0:
                acc_row = n_row
                break
        else:
            return 0
        
        for n_c in range (s[1]):
            temp: int | float = old_matrix[0][n_c]
            old_matrix[0][n_c] = old_matrix[acc_row][n_c]
            old_matrix[acc_row][n_c] = temp
           

        val *= -1

        

    def det_matrix_2x2(m: Macierz) -> int | float:
        if m.size() == (2, 2):
            return m[0][0]*m[1][1] - m[0][1]*m[1][0]
        else:
            raise ValueError('Blędne dane wejśćiowe')
    old_size: Tuple[int, int] = old_matrix.size()

    if old_size == (2, 2):
        last_det: int | float = det_matrix_2x2(old_matrix)
        return last_det/val

    new_size: Tuple[int, int] = (old_size[0]-1, old_size[1]-1)
    new_matrix: Macierz = Macierz(new_size)

    for r in range(new_size[0]):
        for c in range(new_size[1]):
            matrix_to_det: Macierz = Macierz([[old_matrix[0][0], old_matrix[0][c+1]], 
                                     [old_matrix[r+1][0], old_matrix[r+1][c+1]]])
            new_matrix[r][c] = det_matrix_2x2(matrix_to_det)
    val *= old_matrix[0][0]**(old_size[0]-2)

    return Chio(new_matrix, val)

        
    
    


def main():
    mat = Macierz([

    [5 , 1 , 1 , 2 , 3],

    [4 , 2 , 1 , 7 , 3],

    [2 , 1 , 2 , 4 , 7],

    [9 , 1 , 0 , 7 , 0],

    [1 , 4 , 7 , 2 , 2]

    ])

    mat2 = Macierz([
     [0 , 1 , 1 , 2 , 3],
     [4 , 2 , 1 , 7 , 3],
     [2 , 1 , 2 , 4 , 7],
     [9 , 1 , 0 , 7 , 0],
     [1 , 4 , 7 , 2 , 2]
    ])

    print(Chio(mat))
    print(Chio(mat2))
   
 

if __name__ == '__main__':
    main()




        

            
            
            
            




        
