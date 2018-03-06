# Line 2 gives a string for printing under the term formatter
formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
# no "are required around True / False" as Python recognises them as keywords
print(formatter.format(True, False, False, True))
# writting formatter once would mean that there would be 4 * {} as it is written
# mutiple times the {} are 4 * 4
print(formatter.format(formatter, formatter, formatter, formatter))
# formatter is used here and has the variable inside as written within the ""
print(formatter.format(
    "This is line 1",
    "Line 2 and 3",
    "Nothing important",
    "Is written here"
    ))
