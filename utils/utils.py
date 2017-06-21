# @return [List<Char>] A list of all characters in the order of their actual
#                      letter frequency in English.
def english_letter_frequency():
  return ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'R', 'H', 'D', 'L', 'U', 'C',
          'M', 'F', 'Y', 'W', 'G', 'P', 'B', 'V', 'K', 'X', 'Q', 'J', 'Z']

# @param string [String] The sentence to get the letter frequency of
# @return [List<Char>] A list of all characters in the order of their letter
#                      frequency. For equal-value letters, they are ordered
#                      as they appear in the English frequency.
def sentence_letter_frequency(string):
  english = english_letter_frequency()
  plaintext_freq = { letter : 0 for letter in english }
  for char in string:
    if char.upper() in plaintext_freq:
      plaintext_freq[char.upper()] += 1
  letters = sorted(plaintext_freq, key=plaintext_freq.get, reverse=True)

  # @param index [Integer] The frequency of a certain letter in plaintext
  # @return [Integer] The occurence of the given index's letter in the plain
  def plain_index(index):
      return plaintext_freq[letters[index]]

  # @param index [Integer] The frequency of a certain letter in normal English
  # @return [Integer] The index of the given plaintext letter index
  def english_index(index):
      return frequency.index(letters[index])

  count = 0
  while count < len(letters) - 1:
      if plain_index(count) == plain_index(count + 1) and \
         english_index(count) > english_index(count + 1):
        letters[count], letters[count + 1] = letters[count + 1], letters[count]
        if count:
          count -= 1
      else:
        count += 1
  return letters
