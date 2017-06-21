from re import match

from structures.basenum import BaseNum

class OctNum(BaseNum):
  BASE = 8
  FORMAT = '{0:o}'
  ENCODING = 'oct'
  REGEX = r'^[0-7]*$'

  # @param data [String] The value to represent by the OctNum.
  # @raise [ValueError] If the given value is not valid octal.
  def __init__(self, data):
    data = OctNum.clean_oct_string(data)
    super(OctNum, self).__init__(data)

  # @param string [String] The string to remove the 0 prefix from.
  # @return [String] The string without the 0 prefix.
  @staticmethod
  def clean_oct_string(string):
    if string.startswith('0'):
      return string[len('0'):]
    return string
