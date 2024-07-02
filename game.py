import tkinter as tk
from tkinter import messagebox

# Initializing for player X
first_player = "X"
board = [" " for _ in range(9)] #a list for 3x3 board
buttons = [] #list of buttons for the 9 cells

def create_board(gamewindow):
    for i in range(3): #create button for each cell
        row = []
        for j in range(3):
            button = tk.Button(gamewindow, text=" ", font=('normal', 30, 'normal'), width=4, height=1,
                               command=lambda i=i, j=j: button_click(i, j))
            button.grid(row=i, column=j)
            row.append(button)
        buttons.append(row)

def button_click(i, j):
    global first_player
    if buttons[i][j]["text"] == " " and not check_winner():
        buttons[i][j]["text"] = first_player
        board[i * 3 + j] = first_player
        if check_winner():
            messagebox.showinfo("Tic Tac Toe", f"Player {first_player} wins!")
            reset_board()
        elif " " not in board:
            messagebox.showinfo("Tic Tac Toe", "It's a draw!") #if all cells r filled -draw
            reset_board()
        else:
            first_player = "O" if first_player == "X" else "X" #switch player

def check_winner():
    winif = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]              
    ]
    for combo in winif:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ": #if all X or O and not empty
            return True
    return False

def reset_board():
    global board, first_player
    board = [" " for _ in range(9)]
    first_player = "X"
    for row in buttons:
        for button in row:
            button["text"] = " "


gamewindow = tk.Tk()
gamewindow.title("Tic Tac Toe")

create_board(gamewindow)

gamewindow.mainloop()
