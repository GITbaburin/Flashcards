import tkinter as tk
import random
from dictionary import FLASHCARDS_HSK1


class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chinese Flashcards")

        self.card_front = True
        self.showing_pinyin = False
        self.current_card = 0
        self.random_mode = False

        scale_factor = 1.4

        self.card_label = tk.Label(root, text="", font=("Arial", int(40 * scale_factor)))
        self.card_label.pack(pady=int(20 * scale_factor))

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=int(20 * scale_factor))

        self.flip_button = tk.Button(self.button_frame, text="Flip", command=self.flip_card, font=("Arial", int(16 * scale_factor)))
        self.flip_button.grid(row=0, column=0, padx=int(10 * scale_factor), pady=int(5 * scale_factor))

        self.next_button = tk.Button(self.button_frame, text="Next", command=self.next_card, font=("Arial", int(16 * scale_factor)))
        self.next_button.grid(row=0, column=1, padx=int(10 * scale_factor), pady=int(5 * scale_factor))

        self.pinyin_button = tk.Button(self.button_frame, text="Show Pinyin", command=self.toggle_pinyin, font=("Arial", int(16 * scale_factor)))
        self.pinyin_button.grid(row=0, column=2, padx=int(10 * scale_factor), pady=int(5 * scale_factor))

        self.random_toggle = tk.Checkbutton(root, text="Random", command=self.toggle_random_mode, font=("Arial", int(16 * scale_factor)))
        self.random_toggle.pack(pady=int(10 * scale_factor))

        self.show_card()

    def show_card(self):
        card = FLASHCARDS_HSK1[self.current_card]
        if self.card_front:
            self.card_label.config(text=card['character'])
        else:
            self.card_label.config(text=card['translation'])
        self.showing_pinyin = False
        self.pinyin_button.config(text="Show Pinyin")

    def flip_card(self):
        self.card_front = not self.card_front
        self.show_card()

    def toggle_pinyin(self):
        card = FLASHCARDS_HSK1[self.current_card]
        if self.showing_pinyin:
            self.card_label.config(text=card['character'])
            self.pinyin_button.config(text="Show Pinyin")
        else:
            self.card_label.config(text=card['pinyin'])
            self.pinyin_button.config(text="Show Hanzi")
        self.showing_pinyin = not self.showing_pinyin

    def next_card(self):
        self.card_front = True
        if self.random_mode:
            self.current_card = random.randint(0, len(FLASHCARDS_HSK1) - 1)
        else:
            self.current_card = (self.current_card + 1) % len(FLASHCARDS_HSK1)
        self.show_card()

    def toggle_random_mode(self):
        self.random_mode = not self.random_mode

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()