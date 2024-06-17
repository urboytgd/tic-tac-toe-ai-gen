import tkinter as tk
from tkinter import Toplevel, Button, Label
import random

def init_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def check_win(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player, player, player] in win_conditions

def check_draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def ai_move(board, player):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            board[row][col] = player
            buttons[row][col].config(text=player, state=tk.DISABLED, disabledforeground='white')
            break

def on_click(row, col):
    if board[row][col] == ' ':
        board[row][col] = 'X'
        buttons[row][col].config(text='X', state=tk.DISABLED, disabledforeground='white')

        if check_win(board, 'X'):
            show_result("You win!")
            disable_all_buttons()
            return

        if check_draw(board):
            show_result("The game is a draw!")
            return

        ai_move(board, 'O')

        if check_win(board, 'O'):
            show_result("AI wins!")
            disable_all_buttons()
            return

        if check_draw(board):
            show_result("The game is a draw!")

def disable_all_buttons():
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(state=tk.DISABLED)

def restart_game():
    global board
    board = init_board()
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=' ', state=tk.NORMAL)
    status_label.config(text="Player X's turn")

def show_result(message):
    result_window = Toplevel(root)
    result_window.title("Game Over")
    result_window.configure(bg='white')
    result_window.geometry("300x200")
    result_label = Label(result_window, text=message, font='Helvetica 15 bold', bg='white')
    result_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    restart_button = Button(result_window, text="Restart", font='Helvetica 15 bold', command=lambda: close_result_window(result_window), bg='#4CAF50', fg='white', activebackground='#45a049')
    restart_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    result_window.overrideredirect(True)

def close_result_window(window):
    window.destroy()
    restart_game()

def main():
    global root, board, buttons, status_label

    board = init_board()

    root = tk.Tk()
    root.title("Tic Tac Toe")
    root.configure(bg='white')
    root.geometry("420x480")  # Adjust the window size to fit the buttons properly
    root.resizable(False, False)

    buttons = [[None for _ in range(3)] for _ in range(3)]

    for row in range(3):
        for col in range(3):
            button = tk.Button(root, text=' ', font='Helvetica 20 bold', height=3, width=6,
                               command=lambda r=row, c=col: on_click(r, c),
                               bg='#f0f0f0', fg='black', activebackground='#d9d9d9', relief='flat', borderwidth=2)
            button.grid(row=row, column=col, padx=5, pady=5)
            buttons[row][col] = button

    status_label = tk.Label(root, text="Player X's turn", font='Helvetica 15 bold', bg='white')
    status_label.grid(row=3, column=0, columnspan=3, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
