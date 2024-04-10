import pandas as pd 

# Read csv with morse code alphabet
df = pd.read_csv("morse_code.csv")
MORSE_CODE_DICT = {row.character: row.morse_code for (_, row) in df.iterrows()}
 
def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + '  '  # Note the double space here
        else:
            morse_code += ' '
    return morse_code.strip()
 
 
def morse_to_text(morse_code):
    morse_to_char = {morse: char for char, morse in MORSE_CODE_DICT.items()}
    words = morse_code.split('   /  ')  # Split by ' / ' to separate words
    translated_text = ''
    for word in words:
        chars = word.split("   ")  # Split by single space to separate characters
        print(word)
        print(chars)
        for char in chars:
            translated_text += morse_to_char.get(char, '')  # Map Morse code to character
        translated_text += ' '  # Add space between words
    return translated_text.strip() 
 
def main():
    choice = input("Choose an option:\n1. Text to Morse Code\n2. Morse Code to Text\nEnter choice (1/2): ")
 
    if choice == '1':
        input_text = input("Enter a string: ")
        morse_code = text_to_morse(input_text)
        print("Morse Code:", morse_code)
    elif choice == '2':
        input_morse = input("Enter Morse code: ")
        translated_text = morse_to_text(input_morse)
        print("Translated Text:", translated_text)
    else:
        print("Invalid choice. Please enter 1 or 2.")
 
 
if __name__ == "__main__":
    main()
