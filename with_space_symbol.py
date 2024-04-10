import pandas as pd

df = pd.read_csv("morse_code.csv")
new_dict = {row.character:row.morse_code for (index, row) in df.iterrows()}
# print(new_dict)

print("Unesite vaš tekst a ja ću Vama da napišem kako se to piše koristeći MORSE CODE...")
unos = input().upper() #! obavezno pretvoriti u upper jer su sva slova u dict upper

# morse_code_alphabet = [new_dict[slovo] for slovo in unos if slovo in new_dict]A

# Construct Morse code string
morse_code_alphabet = ''.join([new_dict.get(slovo, '') for slovo in unos])

print(f"Vaša poruka ispisana Morseovim kodom: {morse_code_alphabet}")