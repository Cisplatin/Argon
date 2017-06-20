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
    if not match(self.__class__.REGEX, data):
      raise ValueError('Invalid data given for OctNum.')
    super(OctNum, self).__init__(data)
