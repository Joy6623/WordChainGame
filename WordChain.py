import random
import string
import time

size = 8
grid = []
selected = []
score = 0
power_ups = {'shuffle': 1, 'freeze': 1, 'bomb': 1}
frozen = False
freeze_end = 0
words = set()

# determine whether the words spelled by the player exist
def load_words():
    global words
    try:
        with open('words.txt', encoding='utf-8') as f:
            words = {w.strip().lower() for w in f if len(w.strip()) >= 3}
        print(f"Loaded {len(words)} words.")
    except FileNotFoundError:
        print("words.txt not found. Using fallback set.")
        words = {
            'ball', 'bar', 'bird', 'book', 'boy', 'car', 'cat', 'code', 'dog',
            'door', 'draw', 'fish', 'food', 'game', 'girl', 'hat', 'jump',
            'man', 'moon', 'play', 'read', 'room', 'run', 'sing', 'star',
            'sun', 'swim', 'talk', 'tree', 'walk', 'wall', 'write'
        }

# Generate a random letter grid containing vowels and consonants
def init_grid():
    global grid
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    grid = []
    for _ in range(size):
        row = []
        for _ in range(size):
            if random.random() < 0.3:
                row.append(random.choice(vowels))
            else:
                row.append(random.choice(consonants))
        grid.append(row)

# Print the grid, score and control prompts
def display_grid():
    print("\n" + "=" * 40)
    print(f"Score: {score} | Power-ups: {power_ups}")
    print("   " + " ".join(chr(ord('a') + i) for i in range(size)))
    for y in range(size):
        line = f"{y+1:2d} " + " ".join(grid[y][x].upper() for x in range(size))
        print(line)
    sel = "".join(grid[y][x].upper() for x, y in selected)
    print("Selected:", sel)
    print("Controls: Row numbers 1-8 + column letters a-h, e: judgment, s: shuffling, f: freezing, b: bomb, q: exit")
    print("=" * 40)

# Determine whether the selected letter is legal
def is_valid(x, y):
    if not (0 <= x < size and 0 <= y < size):
        return False
    if (x, y) in selected:
        return False
    if not selected:
        return True
    lx, ly = selected[-1]
    return abs(x - lx) <= 1 and abs(y - ly) <= 1

# Check whether the selected letters are legal words. If so, add points and replace the letters.
def check_word():
    global score
    w = "".join(grid[y][x] for x, y in selected).lower()
    if w in words:
        gained = len(w) * 10
        score += gained
        print(f" Word {w.upper()} +{gained} points!")
        for x, y in selected:
            grid[y][x] = random.choice(string.ascii_lowercase)
        return True
    else:
        print(f" {w.upper()} not in dictionary.")
        return False


def use_power(power):
    # Use Props (shuffle, freeze, bomb)
    global frozen, freeze_end, score

    # If the item count is 0, prompt and return
    if power_ups.get(power, 0) == 0:
        print(f"No {power} left!")
        return False  # No prop available, cannot use

    if power == 'shuffle':
        power_ups[power] -= 1  # Use once
        init_grid()  # Regenerate the alphabet
        print("Grid shuffled!")

    elif power == 'freeze':
        power_ups[power] -= 1  # Use once
        frozen = True  # Activate the frozen state
        freeze_end = time.time() + 5
        print("Freeze for 5 seconds!")

    elif power == 'bomb':
        # If no selection, skip without using the prop
        if not selected:
            print("Select letters first to bomb.")
            return False

        power_ups[power] -= 1  # Use once (only after validation)
        # Replace the selected letter with a new random letter to earn 5 points
        for x, y in selected:
            grid[y][x] = random.choice(string.ascii_lowercase)
        score += 5
        print("Bomb used on selection, +5 points!")

    else:
        print("Unknown power-up!")
        return False

    return True  # The prop was used successfully


def play():
    global frozen, selected
    load_words() # Load the word bank
    init_grid() # Initialize the letter grid

    while True:
        display_grid()
        if frozen and time.time() > freeze_end:
            frozen = False
            print("Freeze ended!")

        cmd = input("Move> ").strip().lower()
        if cmd == 'q':
            break
        if not frozen:
            if cmd == 's':
                use_power('shuffle')
            elif cmd == 'f':
                use_power('freeze')
            elif cmd == 'b':
                use_power('bomb')
            elif cmd == 'e':
                if len(selected) >= 3:
                    check_word()
                else:
                    print("At least 3 letters needed.")
                selected = [] # Clear the selected ones
                time.sleep(1)
            elif cmd.isdigit() and 1 <= int(cmd) <= size:
                y = int(cmd) - 1
                col = input("Column (a-h)> ").strip().lower()
                if len(col) == 1 and 'a' <= col <= chr(ord('a') + size - 1):
                    x = ord(col) - ord('a')
                    if is_valid(x, y):
                        selected.append((x, y))
                    else:
                        print("Invalid selection!")
                else:
                    print("Invalid column input!")
            else:
                print("Unknown command!")

            # Low-probability dropping items
            if random.random() < 0.01:
                p = random.choice(list(power_ups.keys()))
                power_ups[p] += 1
                print(f"New power-up: {p}")

    print("Game Over! Final Score:", score)

if __name__ == "__main__":
    play()
