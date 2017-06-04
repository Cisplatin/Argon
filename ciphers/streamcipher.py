from ciphers.cipher import Cipher

class StreamCipher(Cipher):
  def __init__(self, key):
    super(StreamCipher, self).__init__(key)

  # @param text [BaseNum] The plaintext to encrypt
  # @return [BaseNum] The encrypted ciphertext
  def encrypt(self, text):
    return text ^ self.prng.generate_output(len(text))

  # @param text [BaseNum] The ciphertext to decrypt
  # @return [BaseNum] The plaintext decrypted
  def decrypt(self, text):
    return text ^ self.prng.generate_output(len(text))

  # @param prng [PRNG] The PRNG to use for the cipher
  # @param key [BaseNum] The key to use for the cipher
  # @return [StreamCipher] A cipher using the given PRNG
  @staticmethod
  def build_from_prng(prng, key):
    if prng.__name__ == 'RC4':
      from ciphers.rc4 import RC4
      return RC4(key)
    else:
      raise ValueError('Unknown PRNG given.')
