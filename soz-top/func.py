import random
from words import words
def get_word():
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return  word.upper()
def display(user_letters, word):
    display_letter = ""
    for letter in word:
        if letter in user_letters.upper():
            display_letter += letter
        else:
            display_letter += "_"
    return display_letter
word = get_word()
def play():
    word = get_word()
    word_letters = set(word)
    user_letters = ""
    print(f"men{len(word)} ta harfli so'z o'yladim topa olasizmi? ")
    while len(word_letters) > 0:
        print(display(user_letters, word))
        if len(user_letters) > 0:
            print(f"Shu vaqtgacha kiritgan harflaringiz {user_letters}")
        letter = input("Harf kiritng: ").upper()
        if letter in  user_letters:
            print("Bu harfni oldin kiritgansiz boshqa harf kiriting")
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} harfi to'g'ri")
        else:
            print("Bunday harf yo'q")
        user_letters += letter
    print(f"Tabriklayman {word} so'zini {len(user_letters)} ta urinish bilan topdingiz")