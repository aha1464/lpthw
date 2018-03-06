#
from sys import argv
# OS module allows you to interface with underlying operating system.
from os.path import exists
# below are the packages that need to be unpacked
script, from_file, to_file = argv
# print the screen text listed below, {where these are files names listed on running the script}.
print(f"Copying from {from_file} to {to_file}")

# We could do these two on one line, how?
in_file = open(from_file) ; indata = in_file.read()

print(f"The input file is {len(indata)} bytes long)")

print(f"Does the output file exist? {exists(to_file)}")
# comment this out so it won't run print
# (f"Ready, hit RETURN to continue, CTRL-C to abort.")
# input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
