def matrix_divided(matrix, div):
  for i in range(len(matrix)):
    if not isinstance(matrix[i], list):
      raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for j in range(len(matrix[i])):
      if not isinstance(matrix[i][j], int) and not isinstance(matrix[i][j], float):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
  if not isinstance(div, int) and not isinstance(div, float):
    raise TypeError("div must be a number")
  elif div == 0:
    raise ZeroDivisionError("division by zero")
  for i in range(len(matrix)):
    if len(matrix[i]) != len(matrix[i+1]):
      raise TypeError("Each row of the matrix must have the same size")
  return [[round(matrix[i][j]/div, 2) for j in range(len(matrix[i]))] for i in range(len(matrix))]
