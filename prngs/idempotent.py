from prngs.prng import PRNG

class Idempotent(PRNG):
  # @param bits [Integer] The number of bits to return.
  # @return [BaseNum] The next n-bits of the given seed.
  # @raise [ValueError] If there are not enough bits left.
  def generate_output(self, bits):
    if self.bits + bits > len(self.seed.data):
      raise ValueError('Not enough of the seed left to output.')
    result = self.seed.__class__(self.seed.data[self.bits:self.bits + bits])
    return result
