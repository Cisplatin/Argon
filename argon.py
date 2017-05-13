from math import sqrt

class BaseNum:

  # @param data [String] The number to represent
  def __init__(self, data):
    self.data = data

  def __repr__(self):
    return self.data

  # @return [Integer] The length of the number
  def length(self):
    return len(self.data)

  # @param [Integer] The index of the digit to fetch
  # @return [String] The character at the given index
  def at(self, index):
    return self.data[index]

  # @param length [Integer] The desired length of the string, longer than self.
  # @param pad [String] The pad to use. Default is '0'.
  # @return [BaseNum] The number of pads to prepend.
  def pad(self, length, pad='0'):
    return self.__class__((length - self.length()) * pad + self.data)

  # @param str_1 [BaseNum] The first string to make of equal length
  # @param str_2 [BaseNum] The second string to make of equal length
  # @return [BaseNum, BaseNum] The two strings, now of equal length
  @staticmethod
  def normalize_length(str_1, str_2):
    if str_1.length() < str_2.length():
        str_1 = str_1.pad(str_2.length())
    elif str_2.length() < str_1.length():
        str_2 = str_2.pad(str_1.length())
    return str_1, str_2

class HexNum(BaseNum):
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
  def bitwise_xor(str_1, str_2):
    return BinNum.bitwise_and(str_1.to_bin(), str_2.to_bin()).to_hex()

class BinNum(BaseNum):
  BASE = 2

  # @return [List<Boolean>] The bits associated with self.data
  def bits(self):
    return map(int, list(self.data))

  # @return [HexNum] The hexadecimal string representing self.data
  def to_hex(self):
    return HexNum('{0:x}'.format(int(self.data, self.BASE)))

  # @param func [Bool x Bool -> Bool] The bitwise function to perform
  # @param str_1 [BinNum] The first string to bitwise operate on
  # @param str_2 [BinNum] The second string to bitwise operate on
  # @return [BinNum] The result of func(str_1, str_2)
  @staticmethod
  def bitwise(func, str_1, str_2):
    str_1, str_2 = BinNum.normalize_length(str_1, str_2)
    bits = map(lambda x: func(*x), zip(str_1.bits(), str_2.bits()))
    return BinNum(''.join(map(str, bits)))

  # @param str_1 [BinNum] The first string to XOR with
  # @param str_2 [BinNum] The second string to XOR with
  # @return [BinNum] The result of str_1 ^ str_2
  @staticmethod
  def bitwise_xor(str_1, str_2):
    return BinNum.bitwise(lambda x, y: x ^ y, str_1, str_2)

  # @param str_1 [BinNum] The first string to AND with
  # @param str_2 [BinNum] The second string to AND with
  # @return [BinNum]  The result of str_1 & str_2
  @staticmethod
  def bitwise_and(str_1, str_2):
    return BinNum.bitwise(lambda x, y: x & y, str_1, str_2)
