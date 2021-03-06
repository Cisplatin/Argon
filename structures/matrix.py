from utils.utils import dot_product

class Matrix(object):
  # @param rows [Integer] The number of rows required for the matrix.
  # @param cols [Integer] The number of columns required for the matrix.
  # @param value [Element || None] The value to instantiate the matrix with.
  # @raise [ValueError] If a dimension is non-positive.
  def __init__(self, rows, cols, value=None):
    if rows <= 0 or cols <= 0:
      raise ValueError('Cannot create matrix with non-positive dimensions.')
    self.matrix = [[value for i in xrange(cols)] for j in xrange(rows)]

  # @param dimensions [Integer] The length of a row/column for the matrix.
  # @return [Matrix] The identity matrix with the given dimensions.
  # @raise [ValueError] If the dimension is non-positive.
  @staticmethod
  def identity(dimensions):
    matrix = Matrix(dimensions, dimensions, 0)
    for index in xrange(dimensions):
      matrix[index][index] = 1
    return matrix

  # @return [String] The data representation.
  def __repr__(self):
    return '\n'.join(map(lambda x: ' '.join(map(str, x)), self.matrix))

  # @return [Matrix] A copy of the current matrix.
  def copy(self):
    return self.__map(lambda x: x)

  # @return [Integer] The number of rows in the matrix.
  def rows(self):
    return len(self.matrix[0]) if self.matrix != [] else 0

  # @return [Integer] The number of columns in the matrix.
  def cols(self):
    return len(self.matrix)

  # @param index [Integer] The index of the row to return.
  # @return [Array<Element>] The requested row.
  # @raise [IndexError] If the index is out-of-bounds.
  def row(self, index):
    self.check_row_index(index)
    return self.matrix[index]

  # @param index [Integer] The index of the column to return.
  # @return [Array<Element>] The requested column.
  # @raise [IndexError] If the index is out-of-bounds.
  def col(self, index):
    self.check_col_index(index)
    return map(lambda row: row[index], self.matrix)

  # @param index [Integer] The index to check validity for.
  # @return [True] If the index is a valid index.
  # @raise [IndexError] If the index is out-of-bounds.
  def check_row_index(self, index):
    if index < 0 or index >= self.rows():
      raise IndexError('Index out-of-bounds.')
    return True

  # @param index [Integer] The index to check validity for.
  # @return [True] If the index is a valid index.
  # @raise [IndexError] If the index is out-of-bounds.
  def check_col_index(self, index):
    if index < 0 or index >= self.cols():
      raise IndexError('Index out-of-bounds.')
    return True

  # @param row_1 [Integer] The index of the first row to swap.
  # @param row_2 [Integer] The index of the second row to swap.
  # @return [Matrix] The matrix with the two rows swapped.
  def swap_rows(self, row_1, row_2):
    self.check_row_index(row_1) and self.check_row_index(row_2)
    result = self.copy()
    for index in xrange(self.cols()):
      result.matrix[row_1][index] = self.matrix[row_2][index]
      result.matrix[row_2][index] = self.matrix[row_1][index]
    return result

  # @param row [Integer] The index of the row to multiply.
  # @param scalar [Element] The scalar to multiply the row by.
  # @return [Matrix] The matrix with the row multiplied by the given scalar.
  def multiply_row(self, row, scalar):
    self.check_row_index(row)
    result = self.copy()
    for index in xrange(self.cols()):
      result.matrix[row][index] *= scalar
    return result

  # @param row_1 [Integer] The index of the row to add to.
  # @param row_2 [Integer] The index of the row to add from.
  # @return [Matrix] The matrix with the rows added.
  def add_rows(self, row_1, row_2):
    self.check_row_index(row_1) and self.check_row_index(row_2)
    result = self.copy()
    for index in xrange(self.cols()):
      result.matrix[row_1][index] += result.matrix[row_2][index]
    return result

  # @return [Matrix] The transposed matrix.
  def transpose(self):
    result = Matrix(self.cols(), self.rows())
    for row in xrange(self.rows()):
      for col in xrange(self.cols()):
        result[col][row] = self.matrix[row][col]
    return result

  # @return [Element] The determinant of the matrix.
  # @raise [ValueError] If the matrix is not square.
  def determinant(self):
    if self.rows() != self.cols():
      raise ValueError('Cannot find the determinant of non-square matrix.')
    # @param matrix [Array<Array<?>>] The matrix to find the determinant of.
    def recurse_determinant(matrix):
      if len(matrix) == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
      determinant = 0
      for row in xrange(len(matrix)):
        new_matrix = map(lambda x: x[1:], matrix[0:row] + matrix[row + 1:])
        sub_determinant = matrix[row][0] * recurse_determinant(new_matrix)
        determinant += sub_determinant * (1 if row % 2 == 0 else -1)
      return determinant
    if self.rows() == 1:
      return self[0][0]
    return recurse_determinant(self.matrix)

  # @param func [Element -> Element] The function to operate with.
  # @return [Matrix] The result of the matrix after applying the function.
  def __map(self, func):
    result = Matrix(self.rows(), self.cols())
    for row in xrange(self.rows()):
      for col in xrange(self.cols()):
        result[row][col] = func(self[row][col])
    return result

  # @param other [Matrix] The other Matrix to operate on.
  # @param func [Element x Element -> Element] The function to operate with.
  # @return [Matrix] The result of the two Element with the operator.
  # @raise [ValueError] If the two matrices are different dimensions.
  def __operate(self, other, func):
    if self.rows() != other.rows() or self.cols() != other.cols():
      raise ValueError('Cannot operate on matrices with different dimensions.')
    result = Matrix(self.rows(), self.cols())
    for row in xrange(self.rows()):
      for col in xrange(self.cols()):
        result[row][col] = func(self[row][col], other[row][col])
    return result

  # @param other [Matrix] The other Matrix added to.
  # @return [Matrix] The sum of the two Matricies.
  # @raise [ValueError] If the two matricies are different dimensions.
  def __add__(self, other):
    return self.__operate(other, lambda x, y: x + y)

  # @param other [Matrix] The other Matrix subtracted to.
  # @return [Matrix] The difference of the two matrices.
  # @raise [ValueError] If the two Matrices are of different dimensions.
  def __sub__(self, other):
    return self.__operate(other, lambda x, y: x - y)

  # @param other [Matrix] The other Matrix to multiply by.
  # @return [Matrix] The product of the two matrices.
  # @raise [ValueError] If the two Matrices are of incorrect dimensions.
  def __matrix_multiply(self, other):
    if self.cols() != other.rows():
      raise ValueError('Cannot multiply matrices of incorrect dimensions.')
    result = Matrix(self.rows(), other.cols())
    for row in xrange(self.rows()):
      for col in xrange(self.cols()):
        result[row][col] = dot_product(self.row(row), other.col(col))
    return result

  # @param scalar [Element] The scalar to multiply by.
  # @return [Matrix] The scalar multiple of the matrix.
  def __scalar_multiply(self, scalar):
    return self.__map(lambda x: x * scalar)

  # @param other [Element || Matrix] The other Matrix multiplied by (or scalar).
  # @return [Matrix] The product of the two matrices (or matrix and scalar).
  # @raise [ValueError] If both are matrices and are of different dimensions.
  def __mul__(self, other):
    if type(other) == type(self):
      return self.__matrix_multiply(other)
    return self.__scalar_multiply(other)

  # @param other [Element || Matrix] The other Matrix multiplied by (or scalar).
  # @return [Matrix] The product of the two matrices (or matrix and scalar).
  # @raise [ValueError] If both are matrices and are of different dimensions.
  def __rmul__(self, other):
    return self.__mul__(other)

  # @param other [Element] The scalar to divide by.
  # @return [Matrix] The scalar multiple of the matrix.
  def __div__(self, other):
    return self.__map(lambda x: x / other)

  # @param other [Element] The scalar to floor divide by.
  # @return [Matrix] The scalar multiple of the matrix.
  def __floordiv__(self, other):
    return self.__map(lambda x: x // other)

  # @param other [Element] The scalar to modulos by.
  # @return [Matrix] The matrix with each element modulos'd by the scalar given.
  def __mod__(self, other):
    return self.__map(lambda x: x % other)

  # @param other [Matrix] The matrix to indexwise XOR with.
  # @return [Matrix] The result of matrix_1 ^ matrix_2.
  def __xor__(self, other):
    return self.__operate(other, lambda x, y: x ^ y)

  # @param other [Matrix] The matrix to indexwise AND with.
  # @return [Matrix] The result of matrix_1 & matrix_2.
  def __and__(self, other):
    return self.__operate(other, lambda x, y: x & y)

  # @param other [Matrix] The matrix to indexwise OR with.
  # @return [Matrix] The result of matrix_1 | matrix_2.
  def __or__(self, other):
    return self.__operate(other, lambda x, y: x | y)

  # @param index [Integer] The index of the desired row.
  # @return [Array<Element>] The desired row.
  # @raise [IndexError] If the index is out-of-bounds.
  def __getitem__(self, index):
    return self.row(index)

  # @param row [Integer] The index of the desired row to set.
  # @param col [Integer] The index of the desired column to set.
  # @param value [Element] The value to set the index to.
  # @raise [InexError] If the index is out-of-bounds.
  def __setitem__(self, row, col, value):
    self.check_row_index(row) and self.check_col_index(col)
    self.matrix[row][col] = value
