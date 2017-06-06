from abc import ABCMeta, abstractmethod

class PRNG(object):
  __metaclass__ = ABCMeta

  def __init__(self, seed):
    self.seed = seed
    self.bits = 0
    self.prepare_generator()

  # @note Placeholder in case a sub-class does not require preparation.
  def prepare_generator(self):
    pass

  # @param bits [Integer] The number of bits to output.
  # @return [BaseNum] The next n-bits of the prng's output for the given seed.
  @abstractmethod
  def generate_output(self, bits):
    pass

  # @param bits [Integer] The number of bits to output.
  # @return [BaseNum] The next n-bits of the prng's output for the given seed.
  def generate(self, bits):
    result = self.generate_output(bits)
    self.bits += bits
    return result

  # @note Resets the PRNG to start generating outputs from the beginning.
  def reset(self):
    self.__dict__.update(self.__class__(self.seed).__dict__)
