import os
SET_SIZE = 256

SPACE_CHARS = [' ','\t','\n','\r','\f','\v']
DIGIT_CHARS = ['0','1','2','3','4','5','6','7','8','9']
WORD_CHARS = ['_'] + DIGIT_CHARS + [chr(x) for x in range(ord('a'), ord('z')+1)] + [chr(x) for x in range(ord('A'), ord('Z')+1)]

def from_char_list_to_bitvectors(char_list):
    bitvector = [False for _ in range(SET_SIZE)]
    for char in char_list:
        bitvector[ord(char)] = True
    
    complemented = [not x for x in bitvector]
    return bitvector, complemented


def bitvector_to_string(bitvector):
    return ', '.join(['true' if x else 'false' for x in bitvector])

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print(f'Usage: python3 {sys.argv[0]} <output_file>')
        sys.exit(1)

    # Create the folder if it doesn't exist
    os.makedirs(os.path.dirname(sys.argv[1]), exist_ok=True)

    with open(sys.argv[1], 'w') as outfile:
        outfile.write('/* This file is auto-generated by tools/generate_metachar_range.py */\n')
        outfile.write('#pragma once\n')
        outfile.write('#include <vector>\n')
        for name, chars in [('WHITESPACE', SPACE_CHARS), ('WORD', WORD_CHARS), ('DIGIT', DIGIT_CHARS)]:
            bitvector, complemented = from_char_list_to_bitvectors(chars)
            outfile.write(f'const std::vector<bool> {name}_SET({{ {bitvector_to_string(bitvector)} }});\n')
            outfile.write(f'const std::vector<bool> {name}_SET_COMPLEMENTED({{ {bitvector_to_string(complemented)} }});\n')