import structures.basenum

class HexNum(structures.basenum.BaseNum):
  BASE = 16
  FORMAT = '{0:x}'
  ENCODING = 'hex'

  # @return [List<Boolean>] The bits associated with self.data
  def bits(self):
    return self.to_bin().bits()

  # @return [BinNum] The binary string representing self.data
  def to_bin(self):
    from structures.binnum import BinNum
    if self.data == '':
        return BinNum('')
    return BinNum(BinNum.FORMAT.format(int(self.data, self.BASE)))

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
