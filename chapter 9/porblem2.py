'''The game() function in a program lets a user play a game and returns the score as an
integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous
Hi-score. You need to write a program to update the Hi-score whenever the game()
function breaks the Hi-score.'''


import random

def game():
    print("You are Playing a Game...")
    Score = random.randint(1, 100)
# Fetch the high score
    with open("Hi-score.txt") as file:
        highscore = file.read()
    if(highscore != ""):
        highscore = int(highscore)
    else:
        highscore = 0
   
    print(f"Your Score = {Score}")
    if (Score>highscore):
        with open("Hi-score.txt", "w") as file:
            file.write(str(Score))

    return Score
game()