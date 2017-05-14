import structures.basenum
import structures.binnum

BinNum = structures.binnum.BinNum

class HexNum(structures.basenum.BaseNum):
  BASE = 16

  # @return [String] The ASCII string representing self.data
  def to_ASCII(self):
    return self.data.decode('hex')

  # @return [String] The base64 string representing self.data
  def to_base64(self):
    return self.data.decode('hex').encode('base64')

  # @return [BinNum] The binary string representing self.data
  def to_bin(self):
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
