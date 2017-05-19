from structures.basenum import BaseNum
from utils.constants import Constants

# @param seed [BaseNum] The seed to use for the key-scheduing.
# @return [Array<Integer>] The result of the RC4 key-scheduling algorithm
def __key_scheduling(seed):
  key = range(Constants.MAX_BYTE)
  shuffle = 0
  for index in xrange(Constants.MAX_BYTE):
    byte = seed.get_byte(index % seed.bytes()).to_integer()
    shuffle = (shuffle + key[index] + byte) % Constants.MAX_BYTE
    key[index], key[shuffle] = key[shuffle], key[index]
  return key

# @param seed [BaseNum] The seed to use RC4's PRNG with.
# @param bits [Integer] The number of bits to return.
# @return [BaseNum] The first n-bits of RC4's output for the given seed.
def RC4(seed, bits):
  # TODO: Finish this.
  pass

# @param seed [BaseNum] The seed to use RC4A's PRNG with.
# @param bits [Integer] The number of bits to return.
# @return [BaseNum] The first n-bits of RC4A's output for the given seed.
def RC4A(seed, bits):
  # TODO: Finish this.
  pass
