class Matrix(object):
  # @param rows [Integer] The number of rows required for the matrix.
  # @param cols [Integer] The number of columns required for the matrix.
  # @param value [BaseNum || None] The value to instantiate the matrix with.
  def __init__(self, rows, cols, value=None):
    self.rows = rows
    self.cols = cols
    self.matrix = [[value for i in xrange(self.cols)] for j in xrange(self.rows)]

  # @return [String] The data representation.
  def __repr__(self):
    return '\n'.join(map(lambda x: ' '.join(map(str, x)), self.matrix))

  # @return [Matrix] The transposed matrix.
  def transpose(self):
    result = Matrix(self.cols, self.rows)
    for row in xrange(self.rows):
      for col in xrange(self.cols):
        result[col][row] = self.matrix[row][col]
    return result

  # @param other [Matrix] The other Matrix to operate on.
  # @param func [BaseNum x BaseNum -> BaseNum] The function to operate with.
  # @return [Matrix] The result of the two BaseNum with the operator.
  # @raise [ValueError] If the two matrices are different dimensions.
  def __operate(self, other, func):
    if self.rows != other.rows or self.cols != other.cols:
      raise ValueError('Cannot operate on matrices with different dimensions.')
    result = Matrix(self.rows, self.cols)
    for row in xrange(self.rows):
      for col in xrange(self.cols):
        result[row][col] = func(self[row][col], other[row][col])
    return result

  # @param other [Matrix] The other Matrix added to.
  # @return [Matrix] The sum of the two Matricies.
  # @raise [ValueError] If the two matricies are different dimensions.
  def __add__(self, other):
    return self.__operate(other, lambda x, y: x + y)

  # @param other [Matrix] The other Matrix subtracted to.
  # @return [Matrix] The difference of the two Matrixs.
  # @raise [ValueError] If the two Matrices are of different types.
  def __sub__(self, other):
    return self.__operate(other, lambda x, y: x - y)

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
  # @return [Array<BaseNum>] The desired row.
  # @raise [IndexError] If the index is out-of-bounds.
  def __getitem__(self, index):
    if index < 0 or index >= self.rows:
      raise IndexError('Index out-of-bounds.')
    return self.matrix[index]

  # @param row [Integer] The index of the desired row to set.
  # @param col [Integer] The index of the desired column to set.
  # @param value [BaseNum] The value to set the index to.
  # @raise [InexError] If the index is out-of-bounds.
  def __setitem__(self, row, col, value):
    if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
      raise IndexError('Index out-of-bounds.')
    self.matrix[row][col] = value
