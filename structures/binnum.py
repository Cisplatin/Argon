from re import match

from structures.basenum import BaseNum

class BinNum(BaseNum):
  BASE = 2
  FORMAT = '{0:b}'
  ENCODING = 'bin'
  REGEX = r'^[01]*$'

  # @return [List<Boolean>] The bits associated with self.data.
  def bits(self):
    return map(int, list(self.data))

 # @return [Bool] The parity of the string. False if even, True if odd.
  def parity(self):
    return reduce(lambda x, y: x ^ bool(y), self.data, False)

  # @param func [Bool x Bool -> Bool] The bitwise function to perform.
  # @param str_1 [BinNum] The first string to bitwise operate on.
  # @param str_2 [BinNum] The second string to bitwise operate on.
  # @return [BinNum] The result of func(str_1, str_2).
  @staticmethod
  def bitwise(func, str_1, str_2):
    str_1, str_2 = BinNum.normalize_length(str_1, str_2)
    bits = map(lambda x: func(*x), zip(str_1.bits(), str_2.bits()))
    return BinNum(''.join(map(str, bits)))

  # @param other [BinNum] The string to XOR with.
  # @return [BinNum] The result of str_1 ^ str_2.
  def __xor__(self, other):
    return self.__class__.bitwise(lambda x, y: x ^ y, self, other)

  # @param other [BinNum] The string to AND with.
  # @return [BinNum]  The result of str_1 & str_2.
  def __and__(self, other):
    return self.__class__.bitwise(lambda x, y: x & y, self, other)

  # @param other [BinNum] The string to OR with.
  # @return [BinNum]  The result of str_1 | str_2.
  def __or__(self, other):
    return self.__class__.bitwise(lambda x, y: x | y, self, other)
