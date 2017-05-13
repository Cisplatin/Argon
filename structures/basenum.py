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
        return str_1.pad(str_2.length()), str_2
    elif str_2.length() <= str_1.length():
        return str_1, str_2.pad(str_1.length())
