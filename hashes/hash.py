from abc import ABCMeta, abstractmethod

class Hash(object):
  __metaclass__ = ABCMeta

  # @param hash_input [BaseNum] The BaseNum to find the hash of.
  # @return [BaseNum] The output of the hash.
  @abstractmethod
  def hash(self, hash_input):
    pass
