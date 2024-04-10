import pandas as pd
import time
from tkinter import *
import simpleaudio as sa
import os

# ---------------------------- Audio Set Up --------------------------- #
long_audio = os.path.dirname(__file__) + '/long.wav'
short_audio = os.path.dirname(__file__) + '/short.wav'

# ---------------------------- Morse Code Dict ------------------------ #
# Read csv with morse code alphabet
df = pd.read_csv("morse_code.csv")
MORSE_CODE_DICT = {row.character: row.morse_code for (_, row) in df.iterrows()}

# ---------------------------- FUNCTION SETUP -------------------------- #
# Load the audio file
def test_play_sound(filepath):
    wave_obj = sa.WaveObject.from_wave_file(filepath)
    play_obj = wave_obj.play()
    play_obj.wait_done()

# Clear explanatory texts
def clear_text(event=None):
    global widgets_cleared
    # Check if the widgets have not been cleared yet
    if not widgets_cleared:
        text.delete('1.0', END)  # Clear the text widget
        morse_code.delete('1.0', END)  # Clear the morse code widget
        widgets_cleared = True  # Update the flag to indicate that the widgets have been cleared  

# Convert text to morse code
def text_to_morse(event):
    for _ in morse_code_label:
        morse_code_label[_].config(bg='green', fg='black')
    
    input_text = event.widget.get('1.0', END)
    input_text = input_text.upper()
    morse_code_text = ''
    for char in input_text:
        if char in MORSE_CODE_DICT:
            morse_code_text += MORSE_CODE_DICT[char] + ' '
        elif char == '\n':
            continue
        else:
            morse_code_text += char + ' '

    if event.char.upper() in MORSE_CODE_DICT:
        morse_code_label[event.char.upper()].config(bg='black', fg='white')
        window.after(300, lambda: morse_code_label[event.char.upper()].config(bg='green', fg='black'))     
    
    morse_code.delete('1.0', END)
    morse_code.insert('1.0', morse_code_text.strip())
    

# Conver morse code to text
def morse_to_text(event):
    morse = event.widget.get('1.0', END)
    if not morse.strip():  # Handle empty input
        return
    
    words = morse.strip().replace(".", "•").split('   ')  # Split by space between words in Morse code
    message = []
    for word in words:
        chars = word.split()  # Split Morse code word into individual characters
        for char in chars:
            try:
                decoded_char = [key for key, value in MORSE_CODE_DICT.items() if value == char][0]
                message.append(decoded_char)
            except IndexError:
                message.append("[Unknown]")  # Add placeholder for unknown Morse code characters
        message.append(' ')  # Add space between words
    decoded_message = ''.join(message).rstrip()  # Join the decoded message and remove trailing whitespace
    text.delete('1.0', END)
    text.insert('1.0', decoded_message)

# Play audio file
def play_sound():
    codes = morse_code.get('1.0', END).strip()
    for code in codes:
        if code == '•':
            test_play_sound(short_audio)
        elif code == '-':
            test_play_sound(long_audio)
        elif code == ' ':
            time.sleep(1)
        time.sleep(0.1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=5, pady=5, bg='yellow')
window.attributes('-alpha', '0.8')
window.title('Text to Morse Code Converter')
window.iconbitmap('morse-icon.ico')
# window.overrideredirect(True)

# Initialize a flag to keep track of whether the widgets have been cleared or not
widgets_cleared = False

morse_code_label = {}
i = 0
for _ in MORSE_CODE_DICT:
    label = Label(text=f"{_}\n{MORSE_CODE_DICT[_]}", width=6, relief='solid', borderwidth=1)
    label.grid(row=i // 10, column=int(str(i)[-1]))
    morse_code_label[_] = label
    i += 1

text = Text(width=50, height=10)
text.grid(row=7, column=0, columnspan=10,sticky='EW')
text.insert('1.0', 'Click Here and Inser Text to Encode')
window.rowconfigure(7, pad=10)
text.bind('<KeyRelease>', text_to_morse)

morse_code = Text(width=50, height=10)
morse_code.grid(row=8, column=0, columnspan=10, sticky='EW')
morse_code.insert('1.0', 'Enter Morse Code to Decode Separated by Space')
window.rowconfigure(8, pad=10)
morse_code.bind('<KeyRelease>', morse_to_text)

play_button = Button(text='Play', relief='solid', command=play_sound)
play_button.grid(row=9, column=0, columnspan=10, sticky='EW')
  
# Bind the function to left mouse clicks and any key presses
window.bind('<Button-1>', clear_text)
window.bind('<Key>', clear_text)



window.mainloop()