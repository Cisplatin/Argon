from abc import ABCMeta, abstractmethod

class Cipher(object):
  __metaclass__ = ABCMeta

  def __init__(self, key):
    self.key = key

  # @param text [BaseNum] The plaintext to encrypt
  # @return [BaseNum] The encrypted ciphertext
  @abstractmethod
  def encrypt(self, text):
    pass

  # @param text [BaseNum] The ciphertext to decrypt
  # @return [BaseNum] The plaintext decrypted
  @abstractmethod
  def decrypt(self, text):
    pass
