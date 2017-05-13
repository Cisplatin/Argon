import structures.basenum
import structures.binnum

BinNum = structures.binnum.BinNum

class HexNum(structures.basenum.BaseNum):
  BASE = 16

  # @return [String] The base64 string representing self.data
  def to_base64(self):
    return self.data.decode('hex').encode('base64')

  # @return [BinNum] The binary string representing self.data
  def to_bin(self):
    return BinNum('{0:b}'.format(int(self.data, self.BASE)))

  # @param str_1 [HexNum] The first string to XOR with
  # @param str_2 [HexNum] The second string to XOR with
  # @return [HexNum] The result of str_1 ^ str_2
  @staticmethod
  def bitwise_xor(str_1, str_2):
    return BinNum.bitwise_xor(str_1.to_bin(), str_2.to_bin()).to_hex()

  # @param str_1 [HexNum] The first string to AND with
  # @param str_2 [HexNum] The second string to AND with
  # @return [HexNum] The result of str_1 & str_2
  @staticmethod
  def bitwise_and(str_1, str_2):
    return BinNum.bitwise_and(str_1.to_bin(), str_2.to_bin()).to_hex()

  # @param str_1 [HexNum] The first string to OR with
  # @param str_2 [HexNum] The second string to OR with
  # @return [HexNum] The result of str_1 | str_2
  @staticmethod
  def bitwise_or(str_1, str_2):
    return BinNum.bitwise_or(str_1.to_bin(), str_2.to_bin()).to_hex()
