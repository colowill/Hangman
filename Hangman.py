import random
import os

word_database = [
        "dog","cat","fish","book","girl","boy","red","blue","green","home","love","play","happy","friend","apple","orange","guitar","piano","school","window","orange","water","summer","winter","program","kubernetes","software","video","bottle","coffee", "president", "radio", "notebook", "chocolate","memento","psyche","typewriter","keyboard","mouse","confidential","honest","basement","uncommon","archaic","ridiculous", "familiar","obscure","chessboard","swimming","running","jumping","healthy", "galaxy","galvanize","gazebo","giaour","gizmo","glowworm","glyph","gnarly","gnostic","gossip","grogginess","haiku","haphazard","hyphen","iatrogenic","icebox","injury","ivory","ivy","jackpot","jaundice","jawbreaker","jaywalk","jazziest","jazzy","jelly","jigsaw","jinx","jiujitsu","jockey","jogging","joking","jovial","joyful","juicy","jukebox","jumbo","kayak","kazoo","keyhole","khaki","kilobyte","kiosk","kitsch","kiwifruit","klutz","knapsack","larynx","lengths","lucky","luxury","lymph","marquis","matrix","megahertz","microwave","mnemonic","mystify","naphtha","nightclub","nowadays","numbskull","nymph","onyx","ovary","oxidize","oxygen","pajama","peekaboo","phlegm","pixel","pizazz","pneumonia","polka","pshaw","psyche","puppy","puzzling","quartz","queue","quips","quixotic","quiz","quizzes","quorum","razzmatazz","rhubarb","rhythm","rickshaw","schnapps","scratch","shiv","snazzy","sphinx","spritz","squawk","staff","strength","strengths","stretch","stronghold"
        ]

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
guessed_letters = []

response = "blank"
word_target = word_database[random.randint(0,len(word_database))]
word_hidden = []
word_underline = []
word_index = 0

hangman_state = 0
hangman_title = "888    888             d8888      888b    888       .d8888b.            888b     d888             d8888      888b    888 \n888    888            d88888      8888b   888      d88P  Y88b           8888b   d8888            d88888      8888b   888 \n888    888           d88P888      88888b  888      888    888           88888b.d88888           d88P888      88888b  888 \n8888888888          d88P 888      888Y88b 888      888                  888Y88888P888          d88P 888      888Y88b 888 \n888    888         d88P  888      888 Y88b888      888  88888           888 Y888P 888         d88P  888      888 Y88b888 \n888    888        d88P   888      888  Y88888      888    888           888  Y8P  888        d88P   888      888  Y88888 \n888    888       d8888888888      888   Y8888      Y88b  d88P           888       888       d8888888888      888   Y8888 \n888    888      d88P     888      888    Y888       Y8888P88            888       888      d88P     888      888    Y888\n\n"

hangman_title_death = "8888888b.       8888888888             d8888      8888888b.            888b     d888             d8888      888b    888 \n888   Y88b      888                   d88888      888   Y88b           8888b   d8888            d88888      8888b   888 \n888    888      888                  d88P888      888    888           88888b.d88888           d88P888      88888b  888 \n888    888      8888888             d88P 888      888    888           888Y88888P888          d88P 888      888Y88b 888 \n888    888      888                d88P  888      888    888           888 Y888P 888         d88P  888      888 Y88b888 \n888    888      888               d88P   888      888    888           888  Y8P  888        d88P   888      888  Y88888 \n888  .d88P      888              d8888888888      888  .d88P           888       888       d8888888888      888   Y8888 \n8888888P        8888888888      d88P     888      8888888P             888       888      d88P     888      888    Y888\n\n"

for i in range(len(word_target)):
            word_underline.append('___ ')
            word_hidden.append('    ')


def _word_check():
    global hangman_state
    global word_hidden

    if word_target.count(response) > 0:
        for i in range(len(word_target)):
            if word_target[i] == response:
                word_hidden[i] = ' '+response+'  '
                print(word_hidden)
    else:
        print("Guessed wrong!")
        hangman_state += 1

    return

def _state_print():

    os.system("clear")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    if hangman_state == 0:
        print(hangman_title)
        print("\t  _____________________\n\t |\t\t       |\n\t |\t\t       |\n\t |\t\t       |\n\t |\t\t\n\t |\t\t\n\t |\t\t\n\t |\t\t\n\t |\n\t |\n\t |\n\t |\n\t |\n\t |\n\t |\n        /|\\\n       / | \\\n _____/__|__\______\n\n\n")
    elif hangman_state == 1:
        print(hangman_title)
        print("\t  _____________________\n\t |\t\t       |\n\t |\t\t       |\n\t |\t\t     __|__\n \t |\t\t    /^   ^\\\n\t |\t\t   ( e w e )\n\t |\t\t    \_____/\n\t |\t\t\n\t |\t\t\n\t |\t\t\n\t |\t\t\n\t |\t\t\n\t |\t\t\n\t |\t\t\n\t |\n        /|\\\n       / | \\\n _____/__|__\______\n\n\n")
    elif hangman_state == 2:
        print(hangman_title)
        print("\t  _____________________\n\t |\t\t       |\n\t |\t\t       |\n\t |\t\t     __|__\n \t |\t\t    /     \\\n\t |\t\t   ( e _ e )\n\t |\t\t    \_____/\n\t |\t\t       |\n\t |\t\t       |\n\t |\t\t       |\n\t |\t\t       |\n\t |\t\t\n\t |\t\t\n\t |\t\t\n\t |\n        /|\\\n       / | \\\n _____/__|__\______\n\n\n")
    elif hangman_state == 3:
        print(hangman_title)
        print("\t  _____________________\n\t |\t\t       |\n\t |\t\t       |\n\t |\t\t     __|__\n \t |\t\t    /_   _\\\n\t |\t\t   ( e _ e )\n\t |\t\t    \_____/\n\t |\t\t       |\n\t |\t\t       |\n\t |\t\t       |\n\t |\t\t       |\n\t |\t\t      /\n\t |\t\t     /\n\t |\t\t    /\n\t |\n        /|\\\n       / | \\\n _____/__|__\______\n\n\n")
    elif hangman_state == 4:
        print(hangman_title)
        print("\t  _____________________\n\t |\t\t       |\n\t |\t\t       |\n\t |\t\t     __|__\n \t |\t\t    /_   ^\\\n\t |\t\t   ( e _ e )\n\t |\t\t    \_____/\n\t |\t\t       |\n\t |\t\t       |\n\t |\t\t       |\n\t |\t\t       |\n\t |\t\t      / \\\n\t |\t\t     /   \\\n\t |\t\t    /     \\\n\t |\n        /|\\\n       / | \\\n _____/__|__\______\n\n\n")
    elif hangman_state == 5:
        print(hangman_title)
        print("\t  _____________________\n\t |\t\t       |\n\t |\t\t       |\n\t |\t\t     __|__\n \t |\t\t    /^   ^\\\n\t |\t\t   ( O - O )\n\t |\t\t    \_____/\n\t |\t\t  _____|\n\t |\t\t       |\n\t |\t\t       |\n\t |\t\t       |\n\t |\t\t      / \\\n\t |\t\t     /   \\\n\t |\t\t    /     \\\n\t |\n        /|\\\n       / | \\\n _____/__|__\______\n\n\n")
    elif hangman_state == 6:
        print(hangman_title_death)
        print("\t  _____________________\n\t |\t\t       |\n\t |\t\t       |\n\t |\t\t     __|__\n \t |\t\t    /     \\\n\t |\t\t   ( x o x )\n\t |\t\t    \_____/\n\t |\t\t  _____|_____\n\t |\t\t       |\n\t |\t\t       |\n\t |\t\t       |\n\t |\t\t      / \\\n\t |\t\t     /   \\\n\t |\t\t    /     \\\n\t |\n        /|\\\n       / | \\\n _____/__|__\______\n\n\n")

    print("Letter bank:")
    print(''.join(guessed_letters))
    print("\n")
    print(''.join(word_hidden))
    print(''.join(word_underline))
    print("\n\n")


while True:
    _state_print()
    if hangman_state == 6:
        print("Oh no! You lose! The word was: ",word_target)
        break
    response = input("Guess a single letter: ")

    if (len(response) > 1):
        print("Invalid input length!")

    elif response not in alphabet:
        print("Not a letter!")

    elif (len(response) == 1):
        if response in guessed_letters:
            print("You already guessed that letter!")
            hangman_state+=1
            continue
        else:
            guessed_letters.append(response)
            guessed_letters.append(" ")
            _word_check()
            _state_print()
            word_actual = ''.join(word_hidden)
            word_actual = word_actual.replace(" ", "")

            if (word_actual == word_target):
                print("YOU WIN!!!")
                break
        continue
