from utils.utils import dot_product

class Matrix(object):
  # @param rows [Integer] The number of rows required for the matrix.
  # @param cols [Integer] The number of columns required for the matrix.
  # @param value [Element || None] The value to instantiate the matrix with.
  def __init__(self, rows, cols, value=None):
    self.matrix = [[value for i in xrange(cols)] for j in xrange(rows)]

  # @return [String] The data representation.
  def __repr__(self):
    return '\n'.join(map(lambda x: ' '.join(map(str, x)), self.matrix))

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
    if self.check_row_index(index):
      return self.matrix[index]

  # @param index [Integer] The index of the column to return.
  # @return [Array<Element>] The requested column.
  # @raise [IndexError] If the index is out-of-bounds.
  def col(self, index):
    if self.check_col_index(index):
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
  # @raise [IndexError] If one of the indicies is out-of-bounds.
  def swap_rows(self, row_1, row_2):
    # TODO
    pass

  # @return [Matrix] The transposed matrix.
  def transpose(self):
    result = Matrix(self.cols(), self.rows())
    for row in xrange(self.rows()):
      for col in xrange(self.cols()):
        result[col][row] = self.matrix[row][col]
    return result

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
  def matrix_multiply(self, other):
    if self.cols() != other.rows():
      raise ValueError('Cannot multiply matrices of incorrect dimensions.')
    result = Matrix(self.rows(), other.cols())
    for row in xrange(self.rows()):
      for col in xrange(self.cols()):
        result[row][col] = dot_product(self.row(row), other.col(col))
    return result

  # @param scalar [Element] The scalar to multiply by.
  # @return [Matrix] The scalar multiple of the matrix.
  def scalar_multiply(self, scalar):
    return self.__map(lambda x: x * scalar)

  # @param other [Element || Matrix] The other Matrix multiplied by (or scalar).
  # @return [Matrix] The product of the two matrices (or matrix and scalar).
  # @raise [ValueError] If both are matrices and are of different dimensions.
  def __mul__(self, other):
    if type(other) == type(self):
      return self.matrix_multiply(other)
    return self.scalar_multiply(other)

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
    if check_row_index(row) and check_col_index(col):
      self.matrix[row][col] = value
