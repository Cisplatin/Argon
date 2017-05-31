class PRNG(object):
  def __init__(self, seed):
    self.seed = seed
    self.bits = 0

  # @param bits [Integer] The number of bits to output
  # @return [BaseNum] The result of the PRNG with the set seed
  def generate_output(self, bits):
    raise NotImplementedError("Must over-ride generate_output in sub-class.")
