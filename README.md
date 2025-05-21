The program I designed is a text-based word puzzle game named WordChain. It features an 8×8 grid where players select adjacent letters to form valid words from a predefined dictionary. The game includes power-ups: Shuffle (regenerates the grid), Freeze (temporarily halts player input for 5 seconds), and Bomb (replaces selected letters with random ones). Players score 10 points per valid letter used, and power-ups drop randomly with a low probability. The grid is intelligently generated with ~30% vowels to ensure playability.

# For whom：
This game is suitable for language learners, word game enthusiasts and casual players who enjoy puzzle challenges. Whether they are students, office workers or family members, everyone can enhance their vocabulary and thinking response ability through this game. It is suitable for all age groups.

# Why I developed this app：
I developed this game in order to combine learning with entertainment. It can not only train players' spelling and vocabulary recognition abilities, but also enhance the fun and challenge of the game through props and scoring mechanisms, allowing people to learn, relax and improve themselves in a relaxed atmosphere.

# project structure：
WordChain.py 
words.txt 
README.md

# Controls:
Enter row number (1-8)
Enter column letter (a-h)
's' to shuffle the grid
'f' to freeze time
'b' to use bomb
'q' to quit

# Usage
##1️. The game begins
Automatic execution:
Load the word library (from words.txt or the default word library)
Initialize an 8×8 random letter grid
Output effect:
Display the score, the number of props, and the letter grid
Hint: Controls row and column input methods, props (s, f, b, e, q)

##2️. The player selects the letter
Input:
First, enter row numbers 1 to 8, and then enter column numbers a to h
Rule:
The first letter can be chosen arbitrarily;
The subsequent letters must be adjacent to the previous one (up, down, left, right, or slanted).
The same grid cannot be selected repeatedly
Effect:
Display the string composed of the currently Selected letters (such as Selected: C A T)

##3️. Judge whether it is a legal word
Input:
Input e (representing Enter or Evaluate)
Condition:
Choose at least three letters
Effect:
If the spelled word exists in words.txt ➜ bonus points (10 points × number of letters), replace the selected letter
If there is no ➜ display "not in dictionary", no bonus points

##4️. Keep playing
Repeat 2️ and 3️, and continue to choose the letters ➜ to form the word ➜ to judge ➜ score
💥 Special item usage and effects:

🔄 s ➜ Shuffle
Usage time: When good words cannot be spelled out in the grid
Effect:
Shuffle the entire letter grid
Reduce the number of times the item is used by 1

❄️ f ➜ Freeze
Usage time: If you want to extend your thinking time (letters cannot be selected during the freeze period)
Effect:
The grid is frozen within 5 seconds and letters cannot be selected
Prompt "Freeze for 5 seconds!"
Reduce the number of times the item is used by 1

💣 b ➜ Bomb
Usage timing: If some letters have been selected but they are not legal words, these letters can be cleared
Effect:
Replace the selected letter with a random letter
Get a 5-point reward
Reduce the number of times the item is used by 1

🛑 How the game ends
Input: q Exit the game
Effect:
Show the final score. Game Over! Final Score: xxx
