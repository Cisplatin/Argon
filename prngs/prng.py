class PRNG(object):
  def __init__(self, seed):
    self.seed = seed
    self.bits = 0
    self.prepare_generator()

  # @note Placeholder in case a sub-class does not require preparation.
  def prepare_generator(self):
    pass

  # @param bits [Integer] The number of bits to output.
  # @return [BaseNum] The result of the PRNG with the set seed.
  def generate_output(self, bits):
    raise NotImplementedError("Must over-ride generate_output in sub-class.")

  # @note Resets the PRNG to start generating outputs from the beginning.
  def reset(self):
    self.__dict__.update(self.__class__(self.seed).__dict__)
