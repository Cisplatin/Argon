class Cipher(object):
  def __init__(self, key):
    self.seed = seed

  # @param text [BaseNum] The plaintext to encrypt
  # @return [BaseNum] The encrypted ciphertext
  def encrypt(self, text):
    raise NotImplementedError("Must over-ride encrypt in sub-class.")

  # @param text [BaseNum] The ciphertext to decrypt
  # @return [BaseNum] The plaintext decrypted
  def decrypt(self, text):
    raise NotImplementedError("Must over-ride decrypt in sub-class.")
