import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_phonetic_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}

name = input("☕ Enter your name: ").upper()
name_list = [nato_phonetic_alphabet[ch] for ch in name]

print(name_list)
