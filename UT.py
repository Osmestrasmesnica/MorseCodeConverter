from tkinter import *
import os
import pandas as pd

df = pd.read_csv("morse_code.csv")
MORSE_CODE_DICT = {row.character: row.morse_code for (_, row) in df.iterrows()}

window = Tk()
window.config(padx=5, pady=5, bg='yellow')
window.attributes('-alpha', '0.8')
window.title('Text to Morse Code Converter')
# window.overrideredirect(True)

morse_code_label = {}
i = 0
for _ in MORSE_CODE_DICT:
    label = Label(text=f"{_}\n{MORSE_CODE_DICT[_]}", width=6, relief='solid', borderwidth=1)
    label.grid(row=i // 10, column=int(str(i)[-1]))
    morse_code_label[_] = label
    i += 1

text = Text(width=50, height=10)
text.grid(row=7, column=0, columnspan=10,sticky='EW')
text.insert('1.0', 'Enter Text to Encode')
window.rowconfigure(7, pad=10)
# english_text.bind('<KeyRelease>', english_to_morse)

morse_code = Text(width=50, height=10)
morse_code.grid(row=8, column=0, columnspan=10, sticky='EW')
morse_code.insert('1.0', 'Enter Morse Code to Decode Separated by Space')
window.rowconfigure(8, pad=10)
# morse_code.bind('<KeyRelease>', morse_to_english)

play_button = Button(text='Play', relief='solid', command=play_sound)
play_button.grid(row=9, column=0, columnspan=10, sticky='EW')

window.mainloop()
