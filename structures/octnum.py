from re import match

from structures.basenum import BaseNum

class OctNum(BaseNum):
  BASE = 8
  FORMAT = '{0:o}'
  ENCODING = 'oct'
  REGEX = r'^[0-7]*$'
