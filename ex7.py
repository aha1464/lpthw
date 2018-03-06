# print text in line 2 - 4
print("." * 30)
print("Mary had a little lamb.")
print("Its fleece was white as {}. ".format('snow'))
print("And everywhere Mary went.")
# this prints out the . 10 times to show a line od dots to act like a page break
print("." * 30) # what'd that do?
# line 8 -  19 give a value that can then be printed below the dotted line
end1 = "c"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "b"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = '' at the end. try removing it so see what happens. Removing this means that there is a line break bewteen the 2 printed words
print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
