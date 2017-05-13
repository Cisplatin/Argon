import structures.basenum
import structures.hexnum

# TODO: Why won't this line work?
# HexNum = structures.hexnum.HexNum

class BinNum(structures.basenum.BaseNum):
  BASE = 2

  # @return [List<Boolean>] The bits associated with self.data
  def bits(self):
    return map(int, list(self.data))

  # @return [HexNum] The hexadecimal string representing self.data
  def to_hex(self):
    return structures.hexnum.HexNum('{0:x}'.format(int(self.data, self.BASE)))

  # @param func [Bool x Bool -> Bool] The bitwise function to perform
  # @param str_1 [BinNum] The first string to bitwise operate on
  # @param str_2 [BinNum] The second string to bitwise operate on
  # @return [BinNum] The result of func(str_1, str_2)
  @staticmethod
  def bitwise(func, str_1, str_2):
    str_1, str_2 = self.__class__.normalize_length(str_1, str_2)
    bits = map(lambda x: func(*x), zip(str_1.bits(), str_2.bits()))
    return self.__class__(''.join(map(str, bits)))

  # @param str_1 [BinNum] The first string to XOR with
  # @param str_2 [BinNum] The second string to XOR with
  # @return [BinNum] The result of str_1 ^ str_2
  @staticmethod
  def bitwise_xor(str_1, str_2):
    return self.__class__.bitwise(lambda x, y: x ^ y, str_1, str_2)

  # @param str_1 [BinNum] The first string to AND with
  # @param str_2 [BinNum] The second string to AND with
  # @return [BinNum]  The result of str_1 & str_2
  @staticmethod
  def bitwise_and(str_1, str_2):
    return self.__class__.bitwise(lambda x, y: x & y, str_1, str_2)

  # @param str_1 [BinNum] The first string to OR with
  # @param str_2 [BinNum] The second string to OR with
  # @return [BinNum]  The result of str_1 | str_2
  @staticmethod
  def bitwise_or(str_1, str_2):
    return self.__class__.bitwise(lambda x, y: x | y, str_1, str_2)