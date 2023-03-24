'''
This file's purpose is to take a Courier's Code text input from the user and convert it to English text.

Input Type: String
Output Type: String

All dependencies can be found in requirements.txt, which should be pip install -r'd before
running locally.
'''

# note that in this conversion (Courier's Code to English), s/z defaults to s and v/w defaults to w
ENGLISH = {
    '11': 'a' ,
    '12': 'b',
    '13': 'c',
    '14': 'd',
    '15': 'e',
    '16': 'f',
    '21': 'g',
    '22': 'h',
    '23': 'i',
    '24': 'j',
    '25': 'k',
    '26': 'l',
    '31': 'm',
    '32': 'n',
    '33': 'o',
    '34': 'p',
    '35': 'q',
    '36': 'r',
    '41': 's',
    '42': 't',
    '43': 'u',
    '44': 'w',
    '45': 'x',
    '46': 'y',
}

couriers_input = input("Enter the Courier's Code that you would like to translate into English:")

# non-pythonic, how else can I do this?
def couriers_to_english(couriers_code):
    translation = ""
    if couriers_code != None:
        n = len(couriers_code)
        i = 0

        while i < n:
            if couriers_code[i].isnumeric():
                translation += ENGLISH[couriers_code[i:i+2]]
                i += 2
            else:
                translation += couriers_code[i]
                i += 1
    return translation

english_translation = couriers_to_english(couriers_input)

print("Here is the English translation of your Courier's Code:", english_translation)
    