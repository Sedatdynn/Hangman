import random 
from words import words
import string

def get_valid_words(words):
    word = random.choice(words)

    while '-' in word or ' ' in word:#kelime listemiz içerisinde - işareti içeren kelimeler de var.onlar yerine başka kelime seçtik.
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_words(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase) #alfabenin tüm harflerini büyük harf olarak atadık.
    used_letters = set()

    lives = 6

    print("Welcome to HANGMAN. Write 'exit' to end the game.")
    while len(word_letters) > 0 and lives > 0:
        print(f'You have {lives} lives left and you have used these letters: ', ' '.join(used_letters))
        

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('current word:',''.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter == 'EXIT':
            print('exiting..')
            break
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('letter is not in word.')
        elif user_letter in used_letters:
            print('You have already used that character. Please try again..')

        else:
            print('Invalid character. Please try again..')  
       
    if lives == 0:
         print(f'You died. The word was: {word} ')        
    else:
         print(f'you guessed the word, {word}!! ')  
               
hangman()