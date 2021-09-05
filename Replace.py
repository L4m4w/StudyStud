def alphabet_position(text):
    # add a dict with alphabet
    alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,
                'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
                'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18,
                's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,
                'y': 25, 'z': 26}

    without_spaces = text.replace(' ', '')
    dots = without_spaces.replace('.', '')
    spaces = dots.replace("'", '')
    # print(without_spaces)
    lower_all = spaces.lower()
    strip_word = lower_all.replace('', ' ')
    no_word = strip_word.strip()
    split_word = no_word.split(' ')

    # print(split_word)

    digits = []

    for letter in split_word:
        if letter not in alphabet:
            return ''
        else:
            stric = alphabet[letter]
            # print(stric)
            digits.append((stric))
    di = str(digits)
    di1 = di.replace('[', '')
    di2 = di1.replace(']', '')
    di3 = di2.replace(',', '')
    return di3