from abc import ABCMeta, abstractmethod, abstractproperty
from math import log

from utils.constants import Constants

class BaseNum(object):
  __metaclass__ = ABCMeta

  # @note This is the base of the representation used. For example, 16.
  @abstractproperty
  def BASE(self):
    pass

  # @note This is the formatting string used by Python. For example, {0:x}.
  @abstractproperty
  def FORMAT(self):
    pass

  # @note This is the encoding string used by Python. For example, hex.
  @abstractproperty
  def ENCODING(self):
    pass

  # @param data [String] The number to represent
  def __init__(self, data):
    self.data = data

  # @return [String] The data representation.
  def __repr__(self):
    return self.data

  # @return [Integer] The length of the data.
  def __len__(self):
    return len(self.data)

  # @param [Integer] The index of the digit to fetch.
  # @return [String] The character at the given index.
  # @raise [IndexError] If the index is out-of-bounds.
  def at(self, index):
    if index < 0 or index >= len(self):
      raise IndexError('Index out of bounds.')
    return self.data[index]

  # @param length [Integer] The desired length of the string, longer than self.
  # @param pad [String] The pad to use. Default is '0'.
  # @return [BaseNum] The number of pads to prepend.
  # @raise [IndexError] If the index is out-of-bounds.
  def pad(self, length, pad='0'):
    if len(pad) == 0:
      raise IndexError('Cannot have a zero-length pad.')
    padded = self.__class__(((length - len(self) / len(pad))) * pad + self.data)
    return padded.trim(length)

  # @param length [Integer] The maximal length to trim at.
  # @return [BaseNum] The trimmed string.
  # @raise [IndexError] If the index is out-of-bounds.
  def trim(self, length):
    if length < 0 or length > len(self):
      raise IndexError('Index out of bounds.')
    return self.__class__(self.data[:length])

  # @param length [Integer] The final length of the string.
  # @return [BaseNum] The same string but repeated to be of proper length.
  # @raise [IndexError] If the index is out-of-bounds.
  def repeat(self, length):
    if length <= len(self):
      raise IndexError('Repeat length is shorter than string length.')
    return self.pad(length, self.data)

  # @param other [BaseNum] The BaseNum to append.
  # @return [BaseNum] The result of the current BaseNum preppended to the given.
  # @raise [ValueError] If the two BaseNums are of different types.
  def append(self, other):
    if self.__class__ != other.__class__:
      raise ValueError('Cannot append two BaseNums of different types.')
    return self.__class__(self.data + other.data)

  # @return [Integer] The data given as an integer in base 10.
  def to_integer(self):
    return int(self.data, self.__class__.BASE)

  # @param integer [Integer] The integer to convert.
  # @return [BaseNum] The given integer converted into BaseNum.
  # @raise [ValueError] If the integer isn't a positive integer.
  @classmethod
  def from_integer(cls, integer):
    if type(integer) != type(0) or integer < 0:
      raise ValueError('Can only convert positive integer value to BaseNum.')
    return cls(cls.FORMAT.format(integer))

  # @return [String] The data given as ASCII.
  def to_ASCII(self):
    return self.data.decode(self.__class__.ENCODING)

  # @return [BaseNum] The given string converted to a BaseNum.
  @classmethod
  def from_ASCII(cls, string):
    return cls(string.encode(cls.ENCODING))

  # @param str_1 [BaseNum] The first string to make of equal length (padding 0).
  # @param str_2 [BaseNum] The second string to make of equal length.
  # @return [BaseNum, BaseNum] The two strings, now of equal length.
  @staticmethod
  def normalize_length(str_1, str_2):
    if len(str_1) < len(str_2):
        return str_1.pad(len(str_2)), str_2
    elif len(str_2) <= len(str_1):
        return str_1, str_2.pad(len(str_1))

  # @param str_1 [BaseNum] The first number to compare.
  # @param str_2 [BaseNum] The second number to compare (of equal length).
  # @return [Integer] The hamming distance.
  # @raise [ValueError] If strings of unequal length are given.
  @staticmethod
  def hamming_distance(str_1, str_2):
    if len(str_1) != len(str_2):
      raise ValueError('Strings must be equal length.')
    return sum(char_1 != char_2 for char_1, char_2 in zip(str_1, str_2))

  # @param other [BaseNum] The other BaseNum to operate on.
  # @param func [Integer x Integer -> Integer] The function to operate with.
  # @return [BaseNum] The result of the two BaseNum with the operator.
  # @raise [ValueError] If the two BaseNums are of different types.
  def __operate(self, other, func):
    if self.__class__ != other.__class__:
      raise ValueError('Cannot operate on two BaseNums of different types.')
    result = func(self.to_integer(), other.to_integer())
    return self.__class__.from_integer(result)

  # @param other [BaseNum] The other BaseNum added to.
  # @return [BaseNum] The sum of the two BaseNums.
  # @raise [ValueError] If the two BaseNums are of different types.
  def __add__(self, other):
    return self.__operate(other, lambda x, y: x + y)

  # @param other [BaseNum] The other BaseNum subtracted to.
  # @return [BaseNum] The difference of the two BaseNums.
  # @raise [ValueError] If the two BaseNums are of different types.
  def __sub__(self, other):
    return self.__operate(other, lambda x, y: x - y)

  # @param other [BaseNum] The other BaseNum multiplied to.
  # @return [BaseNum] The product of the two BaseNums.
  # @raise [ValueError] If the two BaseNums are of different types.
  def __mul__(self, other):
    return self.__operate(other, lambda x, y: x * y)

  # @param other [BaseNum] The other BaseNum divided to.
  # @return [BaseNum] The quotient of the two BaseNums.
  # @raise [ValueError] If the two BaseNums are of different types.
  def __div__(self, other):
    return self.__operate(other, lambda x, y: x / y)

  # @param other [BaseNum] The other BaseNum floor-divided to.
  # @return [BaseNum] The floored quotient of the two BaseNums.
  # @raise [ValueError] If the two BaseNums are of different types.
  def __floordiv__(self, other):
    return self.__operate(other, lambda x, y: x // y)

  # @param other [BaseNum] The other BaseNum modulos'd to.
  # @return [BaseNum] The modulos of the two BaseNums.
  # @raise [ValueError] If the two BaseNums are of different types.
  def __mod__(self, other):
    return self.__operate(other, lambda x, y: x % y)

  # @param byte [Integer] The byte to get.
  # @return [BaseNum] The n-th byte of self.data.
  # @raise [IndexError] If the byte is out-of-bounds.
  def get_byte(self, byte):
    length = self.length_of_byte()
    num_bytes = self.bytes()

    # If there is an incomplete byte at the end of the data.
    if len(self) % length:
      length += 1
      num_bytes += 1

    if byte >= num_bytes:
      raise IndexError('Index out of bounds.')
    return self.__class__(self.data[byte * length : (byte + 1) * length])

  # @return [Integer] The number of full bytes in the given BaseNum.
  def bytes(self):
    return len(self.data) / self.length_of_byte()

  # @return [Integer] The number of digits in one byte for the type of BaseNum.
  def length_of_byte(self):
    return int(log(Constants.MAX_BYTE, 2) / log(self.__class__.BASE, 2))
