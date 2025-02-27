import tkinter as tk
from tkinter import messagebox
class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.player = "X"
        self.board = ["" for _ in range(9)]
        self.create_widgets()

    def create_widgets(self):
        self.buttons = []
        for i in range(9):
            button = tk.Button(
                self.root, text="", font=("Arial", 24), width=5, height=2,
                command=lambda i=i: self.on_click(i)
            )
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def on_click(self, index):
        if not self.buttons[index]["text"] and not self.check_winner():
            self.buttons[index]["text"] = self.player
            self.board[index] = self.player
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.player} wins!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.player = "O" if self.player == "X" else "X"

    def check_winner(self):
        win_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)              # diagonals
        ]
        return any(
            self.board[a] == self.board[b] == self.board[c] == self.player
            for a, b, c in win_combinations
        )

    def reset_game(self):
        for button in self.buttons:
            button["text"] = ""
        self.board = ["" for _ in range(9)]
        self.player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
