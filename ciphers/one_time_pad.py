# @param text [HexNum] The text to encrypt/decrypt.
# @param key [HexNum] The key to encrypt/decrypt with.
# @return [HexNum] The ciphertext/plaintext
def one_time_pad(text, key):
  return text ^ key.repeat(len(text))
