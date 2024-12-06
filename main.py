
from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#o functie care verifica raspunsul jucatorului cu al programului
def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Numarul e prea mare ! ")
        return turns -1
    elif user_guess < actual_answer:
        print("Numarul este prea mic ! ")
        return turns -1
    else:
        print(f"Ai ghicit ! Raspunsul era {actual_answer} ! ")

# O  functie care seteaza dificultatea
def set_difficulty():
    level = input(f"Alege dificultatea, scrie 'usor' sau 'greu' ! ")
    if level == "usor":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


# alege un numar aleatoriu intre 1 si 100
def game():
    print(logo )
    print("Bun venit la GHICITOAREA DE NUMERE !")
    print("Ma gandesc la un numar cuprins intre 1 si 100...")
    answer = randint(1,100)



    turns = set_difficulty()

    #lasa jucatorul sa ghiceasca un numar
    guess = 0
    while guess != answer:
        print(f"Ai {turns} incercari ca sa ghicesti numarul !")
        guess = int(input("Ghiceste un numar ..."))
        if turns == 0 :
            print("NU mai ai incercari, AI PIERDUT !!! ")
            return
        elif guess != answer :
            print("Ghiceste din nou !")

        turns = check_answer(guess, answer , turns)
game()


