from re import match

from structures.basenum import BaseNum

class HexNum(BaseNum):
  BASE = 16
  FORMAT = '{0:X}'
  ENCODING = 'hex'

  # @param data [String] The value to represent by the HexNum.
  # @raise [ValueError] If the given value is not valid hexadecimal.
  def __init__(self, data):
    if data.startswith('0x'):
      data = data[len('0x'):]
    if not match(r'^[0-9a-fA-F]*$', data):
      raise ValueError('Invalid data given for HexNum.')
    super(HexNum, self).__init__(data)
