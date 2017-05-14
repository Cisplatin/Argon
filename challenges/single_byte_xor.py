from structures.hexnum import HexNum
from utils.utils import letter_frequency

# @param ciphertext [HexNum] The string to decode.
# @return [String] The predicted value of the decrypted ciphertext given that
#                  the cipher used is a single-byte xor.
def single_byte_xor(ciphertext):
  frequency = letter_frequency()
  best_plaintext = None
  best_score = 0

  for i in xrange(ord('a'), ord('z') + 1):

    # Find the XOR of our cipher text with a repeated byte.
    xor = chr(i).encode('hex')
    plaintext = ciphertext ^ HexNum(xor * (len(ciphertext) / len(xor)))
    sentence = plaintext.to_ASCII()

    # Track the frequency of each letter in the ASCII. If an invalid character
    # is found (i.e. a letter before Space in ASCII) then we move onto the next
    # sentence.
    plaintext_freq = { i : 0 for i in frequency }
    invalid_character = False
    for char in sentence:
      if char.upper() in plaintext_freq:
        plaintext_freq[char.upper()] += 1
      elif ord(char.upper()) >= ord(' '):
        invalid_character = True
    if invalid_character:
      continue

    # Find the ordered list of how frequent each letter is. The earlier a letter
    # is in the list, the more common it is.
    letters = sorted(plaintext_freq, key=plaintext_freq.get, reverse=True)

    # @param index [Integer] The frequency of a certain letter in plaintext
    # @return [Integer] The occurence of the given index's letter in the plain
    def plain_index(index):
        return plaintext_freq[letters[index]]

    # @param index [Integer] The frequency of a certain letter in normal English
    # @return [Integer] The index of the given plaintext letter index
    def english_index(index):
        return frequency.index(letters[index])

    # Some letters in the sentence will have the same count. This moves around
    # letters like these so that the array can as close as possible match
    # plaintext_freq's ordering (without ruining the ordering by frequency).
    count = 0
    while count < len(letters) - 1:
        if plain_index(count) == plain_index(count + 1) and \
           english_index(count) > english_index(count + 1):
          letters[count], letters[count + 1] = letters[count + 1], letters[count]
          if count:
            count -= 1
        else:
          count += 1

    # We now judge how valid a sentence is by the distance from the sentence's
    # frequency hash to the English language's frequency hash. The score
    # is the sum of all distances.
    score = sum(map(lambda x: abs(english_index(x) - x), xrange(len(letters))))
    if score > best_score:
      best_plaintext = sentence
      best_score = score

  return best_plaintext
