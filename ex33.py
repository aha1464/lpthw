i = 0
numbers = []

while i < 10:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)

# for-loop can only iterate (loop) "over" collections of things. A while-loop
# cann do any kind of iteration (looping) you want. While-loops are harder
# to get right.

# When a loop runs, it goes through its block of code, and at the end it
# jumps back to the top.

# To visualise this put print statements all over the loop, printing out
# where in the loop python is running and what the variables are set to to,
# at the top of the loop, in the middle, and at the bottom. Study the output
# and try and understand the jumpint that's going on.
