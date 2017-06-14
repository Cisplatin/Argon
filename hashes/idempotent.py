from hashes.hash import Hash

class Idempotent(Hash):
  # @param hash_input [BaseNum] The BaseNum to find the hash of.
  # @return [BaseNum] The string inputted.
  def hash(self, hash_input):
    return hash_input
