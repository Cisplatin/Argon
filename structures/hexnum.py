import structures.basenum

class HexNum(structures.basenum.BaseNum):
  BASE = 16

  # @param integer [Integer] The integer to convert.
  # @return [HexNum] The given integer converted into a HexNum.
  @staticmethod
  def from_integer(integer):
    if type(integer) != type(0) or integer < 0:
      raise ValueError('Cannot convert non-positive integer value to HexNum.')
    return HexNum("{0:x}".format(integer))

  # @return [String] The ASCII string representing self.data
  def to_ASCII(self):
    return self.data.decode('hex')

  # @param string [String] The ASCII string to convert
  # @return [HexNum] The HexNum equivalent of the given ASCII
  @staticmethod
  def from_ASCII(string):
    return HexNum(string.encode('hex'))

  # @return [List<Boolean>] The bits associated with self.data
  def bits(self):
    return self.to_bin().bits()

  # @return [BinNum] The binary string representing self.data
  def to_bin(self):
    from structures.binnum import BinNum
    return BinNum('{0:b}'.format(int(self.data, self.BASE)))

  # @param other [HexNum] The string to XOR with
  # @return [HexNum] The result of str_1 ^ str_2
  def __xor__(self, other):
    return (self.to_bin() ^ other.to_bin()).to_hex()

  # @param other [HexNum] The string to AND with
  # @return [HexNum] The result of str_1 & str_2
  def __and__(self, other):
    return (str_1.to_bin() & str_2.to_bin()).to_hex()

  # @param other [HexNum] The string to OR with
  # @return [HexNum] The result of str_1 | str_2
  def __or__(self, other):
    return (str_1.to_bin() | str_2.to_bin()).to_hex()
