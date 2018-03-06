from sys import argv

script, user_name = argv

# this moves the answer prompt to the questions down a line under the question
prompt = "Type your Answer Here: "
# the print text that we want to display, as well as the variables such as the
# the username and script or file name.
print(f"Hi {user_name}, I'm the {script} script.")
print(f"I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)
# We make a variable, prompt, that is set to the prompt we want, and we give
# that to input instead of typing it over and over. If we want to make the
# prompt something else, we just change it in this one spot and rerun the
# script. Which is cool.
print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)
# using 3 quotations so that we can write the multiline string
print(f"""
    Alright, so you said {likes} about liking me.
    You live in {lives}. Not sure where that is.
    And you have a {computer} computer. Nice!
    """)
