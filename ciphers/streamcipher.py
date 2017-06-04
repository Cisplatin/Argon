from ciphers.cipher import Cipher

class StreamCipher(Cipher):
  def __init__(self, key):
    super(StreamCipher, self).__init__(key)
    self.prng = self.__class__.PRNG(key)

  # @param text [BaseNum] The plaintext to encrypt.
  # @return [BaseNum] The encrypted ciphertext.
  def encrypt(self, text):
    return text ^ self.prng.generate_output(len(text))

  # @param text [BaseNum] The ciphertext to decrypt.
  # @return [BaseNum] The plaintext decrypted.
  def decrypt(self, text):
    return text ^ self.prng.generate_output(len(text))

  # @param prng [PRNG] The PRNG to use for the cipher.
  # @param key [BaseNum] The key to use for the cipher.
  # @return [StreamCipher] A cipher using the given PRNG.
  # @raise [ValueError] If an invalid PRNG is given.
  @staticmethod
  def build_from_prng(prng, key):
    from ciphers.rc4 import RC4
    for klass in StreamCipher.__subclasses__():
      if klass.PRNG.__name__ == prng.__name__:
        return klass(key)
    raise ValueError('Unknown PRNG given.')

  # @note Resets the PRNG to start generating outputs from the beginning.
  def reset(self):
    self.prng.reset()
