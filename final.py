# AF, GW, BO, RC, Build a Game Final
import random
user_name = input("What is your name? ")
scramble = []
with open("stats.txt", "r") as file:
    content = file.read()
    con = content.split(",")
    wins = int(con[0])
    losses = int(con[1])
with open("gabe.txt", "r") as file:
    scrambles = file.read()
    scramble = scrambles.split(",")
word = random.choice(scramble)
moves = 0
at_basement = "0"
at_upstairs = "0"
basment = "0"
upstairs = "0"
with open ("alex.txt", "r") as file:
    content = file.read()
    cipher_file = content.split(",")
random_cipher = random.randint(0,9)
cipher = (cipher_file[random_cipher])
while True:
    if moves <= 10:
        if at_basement == "0" and at_upstairs == "0":
            invintory = []
            num_one = random.randint(0,9)
            num_two = random.randint(0,9)
            num_three = random_cipher
            num_four = 7
            combination = (f"{num_one}{num_two}{num_three}{num_four}")
            print(f"\nYou have won {wins} times and lost {losses} times.\n")
            print("You are walking down the street when all the sudden you are kidnapped and knocked out.")
            print("You wake up to the sound of water dripping to find yourself in a basment... You don't hear anything but you want to be fast.\n\n")
            at_basement = "1"
        if at_basement == "1" and at_upstairs == "0":
            moves += 1
            print('You find yourself in a dark basement. You see two rooms, one with a big "1" on the door, the other with a big "2", and a staircase leading upstairs.')
            basment = input("Do you:\n1) Investigate Room 1\n2) Investigate Room 2\n3) Go upstairs\n")
            if basment == "1":
                while True:
                    # GABE W, This is the first section of the game. If you explore you find a word scramble that gives you the first number for the lock combination when solved.
                    check_basement_one = input("Do you:\n1) Investigate the computer\n2) look behind the corner\n3) leave\n")
                    
                    if check_basement_one == "1":
                        print("On the old dusty computer you find a word scramble")
                        print(f"The word scramble is\n {word}")
                        word_guesst = False
                        while True:
                            word_guesst = False
                            try:
                                def word(word, real_word):
                                    real_word = {
                                        "PPALE": "Apple",
                                        "NABANA": "Banana",
                                        "HCAIR": "Chair",
                                        "OOSLCH": "School",
                                        "RTEAW": "Water",
                                        "REHTACE": "Teacher",
                                        "KOBO": "Book",
                                        "LPEINC": "Pencil",
                                        "WODNWI": "Window",
                                        "RFELOW": "Flower",
                                        "RVIRE": "River",
                                        "TAMOUNIN": "Mountain",
                                        "RAOGNE": "Orange",
                                        "LPEZUZ": "Puzzle",
                                        "RDEGON": "Dragon",
                                        "XEPRENIECE": "Experience",
                                        "EJLYL": "Jelly",
                                        "RTHAE": "Earth",
                                        "DCLUOS": "Clouds",
                                        "NIAR": "Rain",
                                        "HETAR": "Heart",
                                        "LAPENT": "Planet",
                                        "NCOEAS": "Oceans"
                                        
                                    }
                                    if word_guess == real_word:
                                        return print(f"That is correct the number you need is {num_one}")
                                    else:
                                        print("That is not the word")
                                word_guess = input("What is the word?\n").capitalize().strip()
                                if word == "PPALE":
                                    if word_guess == "Apple":
                                        word_guesst == True
                                        print(f"That is correct the number you need is {num_one}")
                                        break
                                elif word == "NABANA":
                                    if word_guess == "Banana":
                                        word_guesst == True
                                        print(f"That is correct the number you need is {num_one}")
                                        break
                                elif word == "HCAIR":
                                    if word_guess == "Chair":
                                        word_guesst == True
                                        print(f"That is correct the number you need is {num_one}")
                                        break
                                elif word == "OOSLCH":
                                    if word_guess == "School":
                                        word_guesst == True
                                        print(f"That is correct the number you need is {num_one}")
                                        break
                                elif word == "RTEAW":
                                    if word_guess == "Water":
                                        word_guesst == True
                                        print(f"That is correct the number you need is {num_one}")
                                        break
                                elif word == "REHTACE":
                                    if word_guess == "Teacher":
                                        word_guesst == True
                                        print(f"That is correct the number you need is {num_one}")
                                        break
                                elif word == "KOBO":
                                    if word_guess == "Book":
                                        word_guesst == True
                                        print(f"That is correct the number you need is {num_one}")
                                        break
                                elif word == "LPEINC":
                                    if word_guess == "Pencil":
                                        word_guesst == True
                                        print(f"That is correct the number you need is {num_one}")
                                        break
                                elif word == "WODNWI":
                                    if word_guess == "Window":
                                        word_guesst == True
                                        print(f"That is correct the number you need is {num_one}")
                                        break
                                elif word == "RFELOW":
                                    if word_guess == "Flower":
                                        word_guesst == True
                                        print(f"That is correct the number you need is {num_one}")
                                        break
                                elif word == "RVIRE":
                                    if word_guess == "River":
                                        word_guesst == True
                                        print(f"That is correct the number you need is {num_one}")
                                        break
                                elif word == "TAMOUNIN":
                                    if word_guess == "Mountain":
                                        word_guesst == True
                                        print(f"That is correct the number you need is {num_one}")
                                        break
                                elif word == "RAOGNE":
                                    if word_guess == "Orange":
                                        word_guesst == True
                                        print(f"That is correct the number you need is {num_one}")
                                        break
                                elif word == "LPEZUZ":
                                    if word_guess == "Puzzle":
                                        word_guesst == True
                                        print(f"That is correct the number you need is {num_one}")
                                        break
                                elif word == "RDEGON":
                                    if word_guess == "Dragon":
                                        word_guesst == True
                                        print(f"That is correct the number you need is {num_one}")
                                        break
                                elif word == "XEPRENIECE":
                                    if word_guess == "Experience":
                                        word_guesst == True
                                        print(f"That is correct the number you need is {num_one}")
                                        break
                                elif word == "EJLYL":
                                    if word_guess == "Jelly":
                                        word_guesst == True
                                        print(f"That is correct the number you need is {num_one}")
                                        break
                                elif word == "RTHAE":
                                    if word_guess == "Earth":
                                        word_guesst == True
                                        print(f"That is correct the number you need is {num_one}")
                                        break
                                elif word == "DCLUOS":
                                    if word_guess == "Clouds":
                                        word_guesst == True
                                        print(f"That is correct the number you need is {num_one}")
                                        break
                                elif word == "NIAR":
                                    if word_guess == "Rain":
                                        word_guesst == True
                                        print(f"That is correct the number you need is {num_one}")
                                        break
                                elif word == "HETAR":
                                    if word_guess == "Heart":
                                        word_guesst == True
                                        print(f"That is correct the number you need is {num_one}")
                                        break
                                elif word == "LAPENT":
                                    if word_guess == "Planet":
                                        word_guesst == True
                                        print(f"That is correct the number you need is {num_one}")
                                        break
                                elif word == "NCOEAS":
                                    if word_guess == "Oceans":
                                        word_guesst == True
                                        print(f"That is correct the number you need is {num_one}")
                                        break
                                else:
                                    print("That is not the word")
                                    continue
                            except:
                                print("Invalid input. Try again.")
                                break
                    if check_basement_one == "2":
                        print("You find a key in a clear locked box. it has a 4 digit code that is needed to open.")
                        lock_input = input("What is the code\n")
                        if lock_input == combination:
                            print("Correct! The box opens and you collect the key inside.")
                            invintory.insert(0, "Key")
                        else:
                            print("Incorrect. You return to the main area.")
                        check_basement_one = "1"
                    if check_basement_one == "3":
                        break
            if basment == "2":
                # BLISS O
                while True:
                    check_basement_two = input("Do you:\n1) Investigate the laptop\n2) Leave\n")
                    if check_basement_two == "1":
                        print("There are some math problems")
                        def addition(num1, num2):
                                    return num1 + num2
                        def subraction(num3, num4):
                                    return num3 - num4
                        def multiplcation(num5, num6):
                                    return num5 * num6
                        def division(num7, num8):
                                    return num7 / num8

                        score = 0
                        while True:

                            def generate_number():
                                number = random.randint(0,15)
                                return number


                            while True:
                                number1 = generate_number()
                                number2 = generate_number()
                                answer = int(input(f"What is {number1} + {number2}? "))
                                if answer == number1 + number2:
                                    print(f"Correct! Next question~")
                                    score += 1
                                else:
                                    print(f"Wrong!!")
                                    score = 0



                                number1 = generate_number()
                                number2 = generate_number()
                                answer = int(input(f"What is {number1} - {number2}? "))
                                if answer == number1 - number2:
                                    print(f"Correct.")
                                    score += 1
                                else:
                                    print(f"Incorrect")
                                    score = 0


                                number1 = generate_number()
                                number2 = generate_number()
                                answer = int(input(f"What is {number1} * {number2}? "))
                                if answer == number1 * number2:
                                    print("Correct!")
                                    score += 1
                                else:
                                    print(f"wrong!")
                                    score = 0

                                while True:
                                    number1 = random.randint(0,15)
                                    number2 = random.randint(1,15)
                                    if number1 % number2 == 0:
                                        break

                                answer = int(input(f"What is {number1} / {number2}? "))
                            
                                if answer == number1 // number2:
                                    print("Correct!!")
                                    score += 1
                                else:
                                    print(f"Incorrect..")
                                    score = 0
                                    
                                print(f"Your final score is: {score}/4")

                                if score == 4:
                                    print(f"You got all the questions right. So as a prize you get the the next digit... {num_two}")
                                    invintory.insert(1, num_two)
                                    break
                                else:
                                    print("You didn't get 4/4 and didn't get the prize. Try again!")
                            break
                    if check_basement_two == "2":
                        break
            if basment == "3":
                at_upstairs = "1"
                at_basement = "0"
        if at_upstairs == "1":
            moves += 1
            print('You find yourself at the front door. Down a hallway, there are two rooms, one with a big "3" on the door, the other with a big "4", and a staircase leading downstairs.')
            upstairs = input("Do you:\n1) Investigate Room 3\n2) Investigate Room 4\n3) Check the door\n4) Go downstairs\n")
            if upstairs == "1":
                # ALEX F
                # This code is for the 3rd part of the combination. It gives the user four options. One for the vending machine, which provides a shifted word and the shift amount, the second for a Bill Cipher easter-egg, the third to go to the caesar cipher, and the fourth to leave the room. The caesar cipher takes an input from the user, a shift amount, and gives the shifed message, which is the number needed.
                print("You enter a mysterious room. In the corner is a vending machine. On the wall, there is a triangular tapestry with an eye in the center. Finally, you see what looks like a cash register on the desk.")
                while True:
                    while True:
                        check_room_one = input("Do you:\n1) Check the vending machine.\n2) Look behind the tapestry.\n3) Investigate the machine on the desk.\n4) Leave\n")
                        if check_room_one not in "1234":
                            print("Invalid input. Try again.")
                        else:
                            break
                    if check_room_one == "1":
                        print(f"You check the vending machine. Engraved into the side is the message {cipher}")
                    if check_room_one == "2":
                        print("Remember! Reality is an illusion, the universe is a hologram, bye gold, BYE!")
                    if check_room_one == "3":
                        while True:
                            use_cipher = input("It is some sort of code-decoder. Use it? (Y) (N)\n")
                            if use_cipher not in "YyNn":
                                print("Invalid input. Try again.")
                            else:
                                break
                        if use_cipher in "Yy":
                            mess = input("Enter your message: ")
                            shift = input("Enter a shift amount: ")
                            def caeser_shift(message, shift):
                                shifted_message = ""
                                for letter in message:
                                    if letter.isalpha():
                                        letter_ascii = ord(letter)
                                        letter_shifted = letter_ascii - shift
                                        if letter.islower():
                                            if letter_shifted > 122:
                                                letter_shifted -= 26
                                            elif letter_shifted < 97:
                                                letter_shifted += 26
                                        if letter.isupper():
                                            if letter_shifted > 90:
                                                letter_shifted -= 26
                                            elif letter_shifted < 65:
                                                letter_shifted += 26
                                        shifted_message += chr(letter_shifted)
                                    else:
                                        shifted_message += letter
                                return shifted_message
                            print(f"The answer is: {caeser_shift(mess, int(shift))}")
                        else:
                            continue
                    if check_room_one == "4":
                        break
            if upstairs == "2":
                # REMY C
                # my code first adds diolouge
                # then my code opens and readsthe remy.txt file which contains the word search
                # then
                print("You walk into the room. On a desk is a peice of paper")
                print('its a word search!?')
                print()
                print('the word search says:')
                print()
                with open("remy.txt", "r") as file:

                    word_search = file.read()

                print(word_search)
                print()
                while True:
                    scrtword = input('what is the secret number. you have 5 guesses (hint it is a number not a word)')
                    if scrtword != "7":
                        print('tell me again')
                        print('you have 4 guesses left')
                        scrtword = input(' what is the secret number')
                    else:
                            print('good job the number was 7')
                            break
                    if scrtword != "7":
                        print('tell me again')
                        print('you have 3 guesses left')
                        scrtword = input(' what is the secret number')
                    else:
                            print('good job the number was 7')
                            break
                    if scrtword != "7":
                        print('tell me again')
                        print('you have 2 guesses left')
                        scrtword = input(' what is the secret number')
                    else:
                            print('good job the number was 7')
                            break
                    if scrtword != "7":
                        print('tell me again')
                        print('you have 1 guesses left')
                        scrtword = input(' what is the secret number')
                    else:
                            print('good job the number was 7')
                            break

                    if scrtword != "7":
                        print('tell me again')
                        print('you have 0 guesses left')
                        print()
                        print('YOU LOST')
                        break
                    else:
                            print('good job the number was 7')
                            break
            if upstairs == "3":
                # ALEX F
                print("You check the door and find that it is locked. You need a key to open it.")
                use_key = input("Do you want to use the key? (Y) (N)\n")
                if use_key in "Yy":
                    if "Key" in invintory:
                        print(f"You use the key to unlock the door. You open it, and find a pile of 1,000 dollars.\n Good job{user_name}! You escaped!")
                        wins += 1
                        with open("stats.txt", "w") as file:
                            file.write(f"{wins},{losses}")
                        play_again = input("Do you want to play again? (Y) (N)\n")
                        if play_again in "Yy":
                            user_name = input("What is your name? ")
                            scramble = []
                            with open("gabe.txt", "r") as file:
                                scrambles = file.read()
                                scramble = scrambles.split(",")
                            word = random.choice(scramble)
                            moves = 0
                            at_basement = "0"
                            at_upstairs = "0"
                            basment = "0"
                            upstairs = "0"
                        else:
                            break
                    else:
                        print("You don't have a key to use.")
            if upstairs == "4":
                at_upstairs = "0"
                at_basement = "1"
    else:
        # ALEX F
        print("The kidnappers return and steal your organs. You lose.")
        losses += 1
        with open("stats.txt", "w") as file:
            file.write(f"{wins},{losses}")
        play_again = input("Do you want to play again? (Y) (N)\n")
        if play_again in "Yy":
            user_name = input("What is your name? ")
            scramble = []
            with open("gabe.txt", "r") as file:
                scrambles = file.read()
                scramble = scrambles.split(",")
            word = random.choice(scramble)
            moves = 0
            at_basement = "0"
            at_upstairs = "0"
            basment = "0"
            upstairs = "0"
            with open ("alex.txt", "r") as file:
                content = file.read()
                cipher_file = content.split(",")
            random_cipher = random.randint(0,9)
            cipher = (cipher_file[random_cipher])
        else:
            print("Thanks for playing!")
            break