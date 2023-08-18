# importing
from tkinter import Tk, Canvas, simpledialog, HIDDEN, NORMAL, Button, Toplevel
from math import floor
from random import choice

# get words and the word
words = []
with open("text.txt") as file:
    for line in file:
        words = (line.rstrip("\n")).split(" ")
word = choice(words)
print(word)


# statistics functions
def find_percentage(x):
    return x / games * 100


def find_rect_length(p):
    return 50 + 2 * p


def reset_and_clear_stats(event=None):
    with open("stats.txt", "w") as file:
        pass
    reset_stats()


# get statistics
stats = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "loss": 0}
games = 0
with open("stats.txt") as file:
    for line in file:
        stats[line.rstrip("\n")] += 1
        games += 1

if games == 0:
    stats_percentage = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "loss": 0}
else:
    stats_percentage = {"1": round(find_percentage(stats["1"]), 1), "2": round(find_percentage(stats["2"]), 1), "3":
        round(find_percentage(stats["3"]), 1), "4": round(find_percentage(stats["4"]), 1), "5":
        round(find_percentage(stats["5"]), 1), "6": round(find_percentage(stats["6"]), 1), "loss":
        round(find_percentage(stats["loss"]), 1)}

# setting up other variables
rounds = 0
press_space__ = 1
current_move_index_squares = 0
current_move_index_letters = 0
move_sequence = [[-5, 0, 0, 0, 0], [-5, -5, 0, 0, 0], [-5, -5, -5, 0, 0], [-5, -5, -5, -5, 0], [-5, -5, -5, -5, -5],
                 [0, -5, -5, -5, -5], [5, 0, -5, -5, -5], [5, 5, 0, -5, -5], [5, 5, 5, 0, -5], [5, 5, 5, 5, 0],
                 [5, 5, 5, 5, 5], [0, 5, 5, 5, 5], [0, 0, 5, 5, 5], [0, 0, 0, 5, 5], [0, 0, 0, 0, 5], [0, 0, 0, 0, 0],
                 [5, 5, 0, 0, 0]]
coords = [(150, 150, 225, 225), (255, 150, 330, 225), (360, 150, 435, 225), (465, 150, 540, 225), (575, 150, 650, 225),
          (150, 250, 225, 325), (255, 250, 330, 325), (360, 250, 435, 325), (465, 250, 540, 325), (575, 250, 650, 325),
          (150, 350, 225, 425), (255, 350, 330, 425), (360, 350, 435, 425), (465, 350, 540, 425), (575, 350, 650, 425),
          (150, 450, 225, 525), (255, 450, 330, 525), (360, 450, 435, 525), (465, 450, 540, 525), (575, 450, 650, 525),
          (150, 550, 225, 625), (255, 550, 330, 625), (360, 550, 435, 625), (465, 550, 540, 625), (575, 550, 650, 625),
          (150, 650, 225, 725), (255, 650, 330, 725), (360, 650, 435, 725), (465, 650, 540, 725), (575, 650, 650, 725)]
wordle_squares = [[], [], [], [], [], []]
wordle_letters = [[], [], [], [], [], []]

# setting up canvas
wordle = Tk()
w = Canvas(wordle, width=800, height=800)

w.create_text(255, 50, anchor="w", fill="black", font="Arial 50 bold", text="WORDLE")
text = w.create_text(200, 775, anchor="w", fill="red", font="Arial 50", text="TOO LITTLE", state=NORMAL)
press_space = w.create_text(62.5, 775, anchor="w", fill="black", font="Arial 30", text="PRESS SPACE TO ENTER A WORD",
                            state=NORMAL)
w.itemconfigure(text, state=HIDDEN)

for x in coords:
    y = floor(coords.index(x) / 5)
    wordle_squares[y].append(w.create_rectangle(x, fill="white", width="10"))
    wordle_letters[y].append(w.create_text(x[0] + 15, x[1], anchor="nw", fill="black", font="Arial 50 bold", text=""))

win_lose_text = w.create_text(175, 430, anchor="w", fill="light blue", font="Arial 75", text="YOU WIN", state=NORMAL)
w.itemconfigure(win_lose_text, state=HIDDEN)
show_stats = Button(wordle, text="SHOW STATS", command=lambda: info.deiconify())
show_stats.place(x=675, y=200)

# the statistics window
info = Toplevel()
i = Canvas(info, width=400, height=300)

rect1 = i.create_rectangle(50, 50, find_rect_length(stats_percentage["1"]), 70, fill="green")
rect2 = i.create_rectangle(50, 80, find_rect_length(stats_percentage["2"]), 100, fill="green")
rect3 = i.create_rectangle(50, 110, find_rect_length(stats_percentage["3"]), 130, fill="green")
rect4 = i.create_rectangle(50, 140, find_rect_length(stats_percentage["4"]), 160, fill="green")
rect5 = i.create_rectangle(50, 170, find_rect_length(stats_percentage["5"]), 190, fill="green")
rect6 = i.create_rectangle(50, 200, find_rect_length(stats_percentage["6"]), 220, fill="green")
rect7 = i.create_rectangle(50, 230, find_rect_length(stats_percentage["loss"]), 250, fill="green")

stats1 = i.create_text(275, 60, text=str(stats_percentage["1"]) + "%", font="Arial 10 bold")
stats2 = i.create_text(275, 90, text=str(stats_percentage["2"]) + "%", font="Arial 10 bold")
stats3 = i.create_text(275, 120, text=str(stats_percentage["3"]) + "%", font="Arial 10 bold")
stats4 = i.create_text(275, 150, text=str(stats_percentage["4"]) + "%", font="Arial 10 bold")
stats5 = i.create_text(275, 180, text=str(stats_percentage["5"]) + "%", font="Arial 10 bold")
stats6 = i.create_text(275, 210, text=str(stats_percentage["6"]) + "%", font="Arial 10 bold")
stats7 = i.create_text(275, 240, text=str(stats_percentage["loss"]) + "%", font="Arial 10 bold")

hide_stats = Button(info, text="HIDE STATS", command=lambda: info.withdraw())
clear_stats = Button(info, text="CLEAR STATS", command=reset_and_clear_stats)
hide_stats.place(x=300, y=50)
clear_stats.place(x=300, y=80)
i.pack()


# main window functions

# gets the guess
def get_guess(event=None):
    if rounds < 6 or press_space__ == 0:
        guess = simpledialog.askstring(title="wordle", prompt="What is your guess?")
        check_guess(guess)


# checks the guess
def check_guess(guess):
    w.itemconfigure(press_space, state=HIDDEN)
    if guess is None:
        pass
    elif len(guess) < 5:
        w.itemconfigure(text, text="TOO LITTLE", state=NORMAL)
        w.after(1000, lambda: w.itemconfigure(text, state=HIDDEN))
    elif len(guess) > 5:
        w.itemconfigure(text, text="TOO MUCH", state=NORMAL)
        w.after(1000, lambda: w.itemconfigure(text, state=HIDDEN))
    elif guess.lower() not in words:
        w.itemconfigure(text, text="NOT VALID", state=NORMAL)
        w.after(1000, lambda: w.itemconfigure(text, state=HIDDEN))
    else:
        generate_clues(guess)


# generates the clues
def generate_clues(guess):
    global rounds
    rounds += 1
    clues_list = []
    for i, x in enumerate(guess):
        if x in word:
            if x == word[i]:
                clues_list.append(2)
            else:
                clues_list.append(1)
        else:
            clues_list.append(0)
    update_gui(clues_list, guess)


# updates the GUI
def update_gui(clues_list, guess):
    global press_space__
    for i, letter in enumerate(wordle_letters[rounds - 1]):
        w.itemconfigure(letter, text=guess[i].upper())
    for i, x in enumerate(wordle_squares[rounds - 1]):
        if clues_list[i] == 0:
            w.itemconfigure(x, fill="gray")
        elif clues_list[i] == 1:
            w.itemconfigure(x, fill="yellow")
        else:
            w.itemconfigure(x, fill="green")
    if guess == word:
        end_sequence("win")
    elif rounds == 6:
        press_space__ = 0
        end_sequence("lose")


# ends the programme
def end_sequence(which):
    global rounds
    win_round = rounds
    rounds = 0
    if which == "win":
        w.itemconfigure(win_lose_text, state=NORMAL, text="YOU WIN")
        win_sequence(win_round)
        with open("stats.txt", "a") as file:
            file.write(str(win_round) + "\n")
    else:
        w.itemconfigure(win_lose_text, state=NORMAL, text="YOU LOSE")
        lose_sequence()
        with open("stats.txt", "a") as file:
            file.write("loss\n")
    w.after(3000, lambda: w.itemconfigure(win_lose_text, state=HIDDEN))
    w.after(4000, play_again__)


# winning animation
def win_sequence(win_round):
    for x in wordle_squares:
        if not wordle_squares.index(x) == win_round - 1:
            for y in x:
                w.itemconfigure(y, fill="white")
    for x in wordle_letters:
        if not wordle_letters.index(x) == win_round - 1:
            for y in x:
                w.itemconfigure(y, text="")
    w.after(1000, lambda: move_squares(move_sequence[0], wordle_squares[win_round - 1]))
    w.after(1000, lambda: move_letters(move_sequence[0], wordle_letters[win_round - 1]))


def move_squares(x, y):
    global current_move_index_squares
    for z, i in enumerate(y):
        w.move(i, 0, x[z])
    current_move_index_squares += 1
    if current_move_index_squares < len(move_sequence):
        w.after(100, move_squares, move_sequence[current_move_index_squares], y)


def move_letters(x, y):
    global current_move_index_letters
    for z, i in enumerate(y):
        w.move(i, 0, x[z])
    current_move_index_letters += 1
    if current_move_index_letters < len(move_sequence):
        w.after(100, move_squares, move_sequence[current_move_index_letters], y)


# losing animation
def lose_sequence():
    delay = 100
    for x in wordle_squares:
        for y in x:
            w.after(delay, lambda y=y: w.itemconfigure(y, fill="red"))
            delay += 100


# asks players if they want to play again
def play_again__():
    y_n = simpledialog.askstring(title="wordle", prompt="Would you like to play again?")
    if y_n is None:
        play_again__()
    elif "y" in y_n.lower():
        reset()
    elif "n" in y_n.lower():
        wordle.destroy()
        info.destroy()
    else:
        play_again__()


# resets the game
def reset():
    global word, rounds, press_space__
    word = choice(words)
    press_space__ = 1
    for x in wordle_squares:
        for y in x:
            w.itemconfigure(y, fill="white")
    for x in wordle_letters:
        for y in x:
            w.itemconfigure(y, text="")
    w.itemconfigure(press_space__, state=NORMAL)
    reset_stats()


def on_closing(event=None):
    global rounds
    if not rounds == 0:
        with open("stats.txt", "a") as file:
            file.write("loss\n")
    wordle.destroy()


# statistics functions

# re-reads stats
def reset_stats():
    global stats, games, stats_percentage, rect1, rect2, rect3, rect4, rect5, rect6, rect7, stats1, stats2, stats3, \
        stats4, stats5, stats6, stats7
    stats = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "loss": 0}
    games = 0
    with open("stats.txt") as file:
        for line in file:
            stats[line.rstrip("\n")] += 1
            games += 1
    if games == 0:
        stats_percentage = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "loss": 0}
    else:
        stats_percentage = {"1": round(find_percentage(stats["1"]), 1), "2": round(find_percentage(stats["2"]), 1), "3":
            round(find_percentage(stats["3"]), 1), "4": round(find_percentage(stats["4"]), 1), "5":
            round(find_percentage(stats["5"]), 1), "6": round(find_percentage(stats["6"]), 1), "loss":
            round(find_percentage(stats["loss"]), 1)}
    rect1 = i.create_rectangle(50, 50, find_rect_length(stats_percentage["1"]), 70, fill="green")
    rect2 = i.create_rectangle(50, 80, find_rect_length(stats_percentage["2"]), 100, fill="green")
    rect3 = i.create_rectangle(50, 110, find_rect_length(stats_percentage["3"]), 130, fill="green")
    rect4 = i.create_rectangle(50, 140, find_rect_length(stats_percentage["4"]), 160, fill="green")
    rect5 = i.create_rectangle(50, 170, find_rect_length(stats_percentage["5"]), 190, fill="green")
    rect6 = i.create_rectangle(50, 200, find_rect_length(stats_percentage["6"]), 220, fill="green")
    rect7 = i.create_rectangle(50, 230, find_rect_length(stats_percentage["loss"]), 250, fill="green")
    stats1 = i.create_text(275, 60, text=str(stats_percentage["1"]) + "%", font="Arial 10 bold")
    stats2 = i.create_text(275, 90, text=str(stats_percentage["2"]) + "%", font="Arial 10 bold")
    stats3 = i.create_text(275, 120, text=str(stats_percentage["3"]) + "%", font="Arial 10 bold")
    stats4 = i.create_text(275, 150, text=str(stats_percentage["4"]) + "%", font="Arial 10 bold")
    stats5 = i.create_text(275, 180, text=str(stats_percentage["5"]) + "%", font="Arial 10 bold")
    stats6 = i.create_text(275, 210, text=str(stats_percentage["6"]) + "%", font="Arial 10 bold")
    stats7 = i.create_text(275, 240, text=str(stats_percentage["loss"]) + "%", font="Arial 10 bold")


info.withdraw()
# setting up canvas contd.
wordle.bind("<space>", get_guess)
wordle.protocol("WM_DELETE_WINDOW", on_closing)
w.pack()
wordle.mainloop()
