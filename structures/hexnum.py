from re import match

from structures.basenum import BaseNum

class HexNum(BaseNum):
  BASE = 16
  FORMAT = '{0:X}'
  ENCODING = 'hex'
  REGEX = r'^[0-9a-fA-F]*$'

  # @param data [String] The value to represent by the HexNum.
  # @raise [ValueError] If the given value is not valid hexadecimal.
  def __init__(self, data):
    data = HexNum.clean_hex_string(data)
    super(HexNum, self).__init__(data)

  # @param string [String] The string to remove 0x prefix from.
  # @return [String] The string without the 0x prefix.
  @staticmethod
  def clean_hex_string(string):
    if string.startswith('0x'):
      return string[len('0x'):]
    return string
