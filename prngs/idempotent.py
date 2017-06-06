from structures.basenum import BaseNum
from prngs.prng import PRNG
from utils.constants import Constants

class Idempotent(PRNG):
  def __init__(self, seed):
    super(Idempotent, self).__init__(seed)

  # @note Resets the PRNG to start generating outputs from the beginning.
  def reset(self):
    self.bits = 0

  # @param bits [Integer] The number of bits to return.
  # @return [BaseNum] The next n-bits of the given seed.
  # @raise [ValueError] If there are not enough bits left.
  def generate_output(self, bits):
    if self.bits + bits > len(self.seed.data):
      raise ValueError('Not enough of the key left to encrypt.')
    result = self.seed.__class__(self.seed.data[self.bits:self.bits + bits])
    self.bits += bits
    return result
