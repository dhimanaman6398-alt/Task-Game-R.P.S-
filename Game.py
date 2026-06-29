import random
import tkinter as tk
from tkinter import messagebox


class RockPaperScissorsGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("CodSoft Task: Rock-Paper-Scissors")
        self.root.geometry("450x550")
        self.root.configure(bg="#2c3e50")
        self.root.resizable(False, False)

        self.user_score = 0
        self.computer_score = 0
        self.ties = 0
        self.choices = ["rock", "paper", "scissors"]
        self.emojis = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}

        self.create_widgets()

    def create_widgets(self):
        
        title_label = tk.Label(
            self.root,
            text="Rock, Paper, Scissors",
            font=("Helvetica", 22, "bold"),
            fg="#ecf0f1",
            bg="#2c3e50",
        )
        title_label.pack(pady=15)

        score_frame = tk.Frame(self.root, bg="#34495e", bd=2, relief=tk.RIDGE)
        score_frame.pack(pady=10, fill=tk.X, padx=20)

        self.score_label = tk.Label(
            score_frame,
            text="Player: 0  |  Computer: 0  |  Ties: 0",
            font=("Helvetica", 14, "bold"),
            fg="#f1c40f",
            bg="#34495e",
            pady=10,
        )
        self.score_label.pack()

        self.result_frame = tk.Frame(self.root, bg="#2c3e50")
        self.result_frame.pack(pady=20)

        self.user_display = tk.Label(
            self.result_frame,
            text="👤\nYou",
            font=("Helvetica", 14),
            fg="#ecf0f1",
            bg="#2c3e50",
            width=12,
        )
        self.user_display.grid(row=0, column=0, padx=20)

        vs_label = tk.Label(
            self.result_frame,
            text="VS",
            font=("Helvetica", 18, "bold"),
            fg="#e74c3c",
            bg="#2c3e50",
        )
        vs_label.grid(row=0, column=1)

        self.computer_display = tk.Label(
            self.result_frame,
            text="🤖\nComputer",
            font=("Helvetica", 14),
            fg="#ecf0f1",
            bg="#2c3e50",
            width=12,
        )
        self.computer_display.grid(row=0, column=2, padx=20)

        self.status_label = tk.Label(
            self.root,
            text="Choose your weapon to start!",
            font=("Helvetica", 14, "italic"),
            fg="#2ecc71",
            bg="#2c3e50",
            pady=15,
        )
        self.status_label.pack()

        btn_frame = tk.Frame(self.root, bg="#2c3e50")
        btn_frame.pack(pady=15)

        btn_styles = {"font": ("Helvetica", 12, "bold"), "width": 10, "pady": 8}

        rock_btn = tk.Button(
            btn_frame,
            text="🪨 Rock",
            bg="#95a5a6",
            fg="black",
            command=lambda: self.play_round("rock"),
            **btn_styles,
        )
        rock_btn.grid(row=0, column=0, padx=10)

        paper_btn = tk.Button(
            btn_frame,
            text="📄 Paper",
            bg="#ecf0f1",
            fg="black",
            command=lambda: self.play_round("paper"),
            **btn_styles,
        )
        paper_btn.grid(row=0, column=1, padx=10)

        scissors_btn = tk.Button(
            btn_frame,
            text="✂️ Scissors",
            bg="#3498db",
            fg="white",
            command=lambda: self.play_round("scissors"),
            **btn_styles,
        )
        scissors_btn.grid(row=0, column=2, padx=10)

        reset_btn = tk.Button(
            self.root,
            text="🔄 Reset Game",
            font=("Helvetica", 11, "bold"),
            bg="#e74c3c",
            fg="white",
            command=self.confirm_reset,
            width=15,
            pady=5,
        )
        reset_btn.pack(pady=25)

    def play_round(self, user_choice):
        computer_choice = random.choice(self.choices)

        self.user_display.config(
            text=f"{self.emojis[user_choice]}\n\nYou Chose:\n{user_choice.capitalize()}"
        )
        self.computer_display.config(
            text=f"{self.emojis[computer_choice]}\n\nComputer Chose:\n{computer_choice.capitalize()}"
        )

        if user_choice == computer_choice:
            self.ties += 1
            self.status_label.config(text="🤝 It's a Tie!", fg="#f1c40f")
        elif (
            (user_choice == "rock" and computer_choice == "scissors")
            or (user_choice == "scissors" and computer_choice == "paper")
            or (user_choice == "paper" and computer_choice == "rock")
        ):
            self.user_score += 1
            self.status_label.config(text="🎉 You Win This Round!", fg="#2ecc71")
        else:
            self.computer_score += 1
            self.status_label.config(
                text="💥 Computer Wins This Round!", fg="#e74c3c"
            )

    
        self.score_label.config(
            text=f"Player: {self.user_score}  |  Computer: {self.computer_score}  |  Ties: {self.ties}"
        )

    def confirm_reset(self):
        
        answer = messagebox.askyesno(
            "Play Again?", "Do you want to clear scores and play another game?"
        )
        if answer:
            self.user_score = 0
            self.computer_score = 0
            self.ties = 0
            self.score_label.config(text="Player: 0  |  Computer: 0  |  Ties: 0")
            self.status_label.config(
                text="Game Reset! Choose your weapon.", fg="#2ecc71"
            )
            self.user_display.config(text="👤\nYou")
            self.computer_display.config(text="🤖\nComputer")
        else:
            self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGUI(root)
    root.mainloop()