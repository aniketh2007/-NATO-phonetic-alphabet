import pandas
#TODO 1. Create a dictionary in this format:

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {rows.letter : rows.code for (index,rows) in data.iterrows() }
print(phonetic_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter the string : ").upper()
output_list = [phonetic_dict[letter] for letter in user_input]
print(output_list)
