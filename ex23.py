# LPTHW EX 23

import sys
# argument variable packages to be unpacked
script, input_encoding, error = sys.argv



def main(language_file, encoding, errors):
    line = language_file.readline()


# first time seeing the if (if line:) if-statement lets you make decisions in your python code
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    # not seen line.strip()
    next_lang = line.strip()
    # MISTAKE puting errors = errors Fixed
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # errors=errors? what is the difference of cooked_string?
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    # what does "<===>" do? Originally was not tabbed in on this line, still didnt work, this is just for printing on screen
    # MISTAKE had a close braket after "<===>)" Fixed
    print(raw_bytes, "<===>", cooked_string)


# utf-8 is the variable width encoding capable of encoding all 1,112,064 valid
# code points in Unicode using one to four 8-bit-bytes
# MISTAKE syntax error: cant assign to function call was given here
# close bracket was in the wrong place ("languages.txt"), encoding="utf-8" Fixed
languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)

# MISTAKE ValueError: not enough values to unpack (expected 3, got 2)
# Fixed, ran with python3.6 ex23.py utf-8 strict

# DBES, decode bytes, encode strings
# Breaking it
# 1. Find strings of text encoded in other encodings and place them in the ex23.py file to see how it breaks
# 2. Find out what happens when you give an encoding that doesn't exist.
# 3. Extra challenging: Rewite this using the 'b' bytes instead of the UTF-8 strings, efectively reversing the script.
# 4. If you can do that, then you can also break these bytes by removing some to see what happens. How much do you need to remove
# to cayse Python to break? How much can you remove to damage the string output but pass Python's decoding system.
# 5. Use what you learned from item 4 to see if you can mangle the files. What errors do you get? How much damage
# can you cayse and get the file past Python's decoding system?
