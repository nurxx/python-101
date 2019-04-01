import sys

def print_hangman():
    print(' _________ ')
    print('|    |    |')
    print('|  \\ O /  |')
    print('|    |    |')
    print('|    |    |')
    print('|   / \\   |')

def hangman(clue_word):
    secret_word=clue_word
    guessing='_ '*len(secret_word)
    print("Welcome to Hangman! Let's play!")
    found=False
    chances=10
    while found == False:
        print(guessing)
        if ''.join(guessing.split()) == secret_word:
            found==True
            print('\nCongratulations!')
            break
        if chances==0:
            print('\nYou lost!')
            print_hangman()
            break
        letter=input('\nGuess a letter: ')
        if letter in secret_word:
            for index,l in enumerate(secret_word):
                if letter == l:
                    guessing=guessing.split()
                    guessing[index]=letter
                    guessing=' '.join(guessing)
        else:
            chances-=1
            print('\nIncorrect!')

def main():
    hangman(sys.argv[1])
    #hangman('chocolate')

if __name__=='__main__':
    main()