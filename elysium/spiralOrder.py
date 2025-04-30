from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    def spiral(matrix):
        if len(matrix) == 1:
            return matrix.pop(0)

        if len(matrix[0]) == 1:
            result = []

            while len(matrix):
                result += matrix.pop(0)

            return result
        
        top, bottom = matrix[0], matrix[-1][::-1]

        result = [] + top

        right = []
        left = []
        for arr in matrix[1:-1]:
            left.append(arr.pop(0))
            right.append(arr.pop(-1))

        matrix.pop(0)
        matrix.pop(-1)

        result += right + bottom + left[::-1]

        return result

    result = []

    while len(matrix):
        if len(matrix[0]) == 0:
            break
            
        result += spiral(matrix)

    return result