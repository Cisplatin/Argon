# @param arg1 [Array<?>] The first list to dot product with.
# @param arg2 [Array<?>] The second list to dot product with.
# @return [?] The dot product of the two arrays.
# @raise [ValueError] If the arrays are of different size.
def dot_product(arg1, arg2):
  if len(arg1) != len(arg2):
    raise ValueError('Cannot dot-product two lists of different length.')
  return sum(map((lambda x: reduce(lambda y, z: y * z, x)), zip(arg1, arg2)))
