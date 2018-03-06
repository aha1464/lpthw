# \t means to tab indent format
tabby_cat = "\tI'm tabbed in."
# \n means a new line so it splits the text into a new line
persian_cat = "I'm split\non a line."
# what the backslashes for?
backslash_cat = "I'm \\ a \\ cat."
# using \t* tabs the txt with a * to format for a list - they are escape esquences
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
