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
