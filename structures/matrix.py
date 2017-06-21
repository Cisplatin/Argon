class Matrix(object):
  # @param rows [Integer] The number of rows required for the matrix.
  # @param cols [Integer] The number of columns required for the matrix.
  # @param value [BaseNum || None] The value to instantiate the matrix with.
  def __init__(self, rows, cols, value=None):
    self.rows = rows
    self.cols = cols
    self.matrix = [[value] * self.cols] * self.rows

  # @param row [Integer] The row index to set.
  # @param col [Integer] The column index to set.
  # @param value [BaseNum] The value to set the matrix to at the row/col.
  # @raise [ValueError] If the index if out-of-bounds.
  def set(self, row, col, value):
    if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
      raise ValueError('Index out-of-bounds.')
    self.matrix[row][col] = value

  # @param row [Integer] The row index to get.
  # @param col [Integer] The column index to get.
  # @raise [ValueError] If the index if out-of-bounds.
  def get(self, row, col):
    if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
      raise ValueError('Index out-of-bounds.')
    return self.matrix[row][col]

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
        result.set(row, col, func(self.get(row, col), other.get(row, col)))
    return result

  # @param other [Matrix] The other Matrix added to.
  # @return [Matrix] The sum of the two Matricies.
  # @raise [ValueError] If the two matricies are different dimensions.
  def __add__(self, other):
    return self.__operate(other, lambda x, y: x + y)