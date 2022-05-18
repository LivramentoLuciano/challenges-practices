# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    def _incrust_char(mychar, mystrings):
        '''Incrusta el caracter "mychar" en todas las posiciones 
        posibles dentro del los strings de la lista "mystrings"'''
        variants = []
        for a_string in mystrings:
            for i in range(len(a_string)+1):
                a_string_list = list(a_string)
                a_string_list.insert(i,mychar)
                a_string_extended = ''.join(a_string_list)
                variants.append(a_string_extended)
        return variants

    # caso base, 1 caracter, fin recursion
    if len(sequence) == 1:
        return [sequence]
    else:
        # Sino -> Recursion
        # Cada 'permutation' resulta de incrustar el 'sequence[0]'
        # en las 'permutaciones' posibles del resto 'sequence[1:]'
        # permutations = []
        # for permutation in get_permutations(sequence[1:]):
        #     permutations.extend(_incrust_char_string(sequence[0], permutation))
        # return permutations
        return _incrust_char(sequence[0], get_permutations(sequence[1:]))


if __name__ == '__main__':
    # EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
    example_input = '123'
    print('Input:', example_input)
    print('Expected Output:', ['123', '132', '213', '231', '312', '321'])
    print('Actual Output:', get_permutations(example_input))

