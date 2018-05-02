class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

print("What is your name?", end='')
# attribute = input (empty)
name = input ()
# key=value container
happy_bday = Song(["Happy birthday to you",
                    "Happy birthday to you",
                    "Happy birthday dear",
                    "Happy birthday to you"])

bulls_on_parade = Song(["They rally round the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

# bulls_on_parade.sing_me_a_song()
