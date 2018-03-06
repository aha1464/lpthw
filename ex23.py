# LPTHW EX 23

import sys
# argument variable packages to be unpacked
script, input_encoding, error = sys.argv



def main(language_file, encoding, errors):
    line = language_file.readline()


# first time seeing the if (if line:)
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    # not seen line.strip()
    next_lang = line.strip()
    # made a mistake here puting errors = errors
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # errors=errors? what is the difference of cooked_string?
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    # what does "<===>" do? Originally was not tabbed in on this line, still didnt work
    print(raw_bytes, "<===>"), cooked_string)


# utf-8 is the variable width encoding capable of encoding all 1,112,064 valid
# code points in Unicode using one to four 8-bit-bytes.
languages = open("languages.txt"), encoding="utf-8"

main(languages, input_encoding, error)
