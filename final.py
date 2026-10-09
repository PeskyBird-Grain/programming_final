# AF, GW, BO, RC, Build a Game Final
import random
user_name = input("What is your name? ")
scramble = []
with open("gabe.txt", "r") as file:
    scrambles = file.read()
    scramble = scrambles.split(",")
word = random.choice(scramble)
# Key room
print("You wake up to the sound of water dripping to find yourself in a basment")

print("You find a word scramble")

print(f"The word scramble is\n {word}")
word_guesst = False
while True:
    word_guest = False
    try:
        word_guess = input("What is the word?\n").capitalize().strip()
        if word == "PPALE":
            if word_guess == "Apple":
                word_guess == True
                print("That is correct the number you need is ___")
                break
        elif word == "NABANA":
            if word_guess == "Banana":
                word_guesst == True
                print("That is correct the number you need is ___")
                break
        elif word == "HCAIR":
            if word_guess == "Chair":
                word_guesst == True
                print("That is correct the number you need is ___")
                break
        elif word == "OOSLCH":
            word_guesst == True
            if word_guess == "School":
                print("That is correct the number you need is ___")
                break
        elif word == "RTEAW":
            if word_guess == "Water":
                word_guesst == True
                print("That is correct the number you need is ___")
                break
        elif word == "REHTACE":
            if word_guess == "Teacher":
                word_guesst == True
                print("That is correct the number you need is ___")
                break
        elif word == "KOBO":
            if word_guess == "Book":
                word_guesst == True
                print("That is correct the number you need is ___")
                break
        elif word == "LPEINC":
            if word_guess == "Pencil":
                word_guesst == True
                print("That is correct the number you need is ___")
                break
        elif word == "WODNWI":
            if word_guess == "Window":
                word_guesst == True
                print("That is correct the number you need is ___")
                break
        elif word == "RFELOW":
            if word_guess == "Flower":
                word_guesst == True
                print("That is correct the number you need is ___")
                break
        elif word == "RVIRE":
            if word_guess == "River":
                word_guesst == True
                print("That is correct the number you need is ___")
                break
        elif word == "TAMOUNIN":
            if word_guess == "Mountain":
                word_guesst == True
                print("That is correct the number you need is ___")
                break
        elif word == "RAOGNE":
            if word_guess == "Orange":
                word_guesst == True
                print("That is correct the number you need is ___")
                break
        elif word == "LPEZUZ":
            if word_guess == "Puzzle":
                word_guesst == True
                print("That is correct the number you need is ___")
                break
        elif word == "RDEGON":
            if word_guess == "Dragon":
                word_guesst == True
                print("That is correct the number you need is ___")
                break
        elif word == "XEPRENIECE":
            if word_guess == "Experience":
                word_guesst == True
                print("That is correct the number you need is ___")
                break
        elif word == "EJLYL":
            if word_guess == "Jelly":
                word_guesst == True
                print("That is correct the number you need is ___")
                break
        elif word == "RTHAE":
            if word_guess == "Earth":
                word_guesst == True
                print("That is correct the number you need is ___")
                break
        elif word == "DCLUOS":
            if word_guess == "Clouds":
                word_guesst == True
                print("That is correct the number you need is ___")
                break
        elif word == "NIAR":
            if word_guess == "Rain":
                word_guesst == True
                print("That is correct the number you need is ___")
                break
        elif word == "HETAR":
            if word_guess == "Heart":
                word_guesst == True
                print("That is correct the number you need is ___")
                break
        elif word == "LAPENT":
            if word_guess == "Planet":
                word_guesst == True
                print("That is correct the number you need is ___")
                break
        elif word == "NCOEAS":
            if word_guess == "Oceans":
                word_guesst == True
                print("That is correct the number you need is ___")
                break
        else:
            print("That is not the word")
            continue
    except:
        print("Invalid input. Try again.")
        break
      
      
 #puzzle room 1
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
    number1 = random.randint(1,12)
    number2 = random.randint(1,12)
    number3 = random.randint(1,12)
    number4 = random.randint(1,12)
    number5 = random.randint(1,12)
    number6 = random.randint(1,20)
    number7 = random.randint(1,20)
    number8 = random.randint(1,20)
   
    addanswer = number1 + number2 
    addition_question = input(f"What is {number1} + {number2}?\n")
    subtraction_question = input(f"What is {number1} - {number2}?\n")
    

    if addition_question == addanswer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect! Try again.")
    
        
    
#Upstairs:
#Room 1:
with open ("alex.txt", "r") as file:
    content = file.read()
    cipher_file = content.split(",")

cipher = random.choice(cipher_file)
while True:
    print("You enter a mysterious room. In the corner is a vending machine. On the wall, there is a triangular tapestry with an eye in the center. Finally, you see what looks like a cash register on the desk.")
    while True:
        check_room_one = input("Do you: 1) Check the vending machine.\n2) Look behind the tapestry.\n3) Investigate the machine on the desk.\n4) Leave\n")
        if check_room_one not in "1234":
            print("Invalid input. Try again.")
        else:
            break
    if check_room_one == "1":
        print(f"You check the vending machine. Engraved into the side is the message {cipher}")
    if check_room_one == "2":
        print("Bill")
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
    else:

#remy room dos:
print('In the room you see a paper on a desk')
print('its a word search!?')
print()
print('S O F T W O O D M A R G O R P')
print('C O M P U T E R N A P W O X L')
print('I W B M G T M L D X B I C E V')
print('E A N T E H R R N Q K S N T I')
print('N C D F V P N B N V X P E S P')
print('C O I Z O G K P F R A H M E R')
print('E B Y S E V E N V E M L T V O')
print('A Z M X L G T N C J N R I E G')
print('B R W W E N L E B H D E U N R')
print('F K V P B U G U S Q D P O N A')
print('A E Q O O N E S M W G W I Y M')
print('E D V R T V H T H U F U Y C R')
print('W K X Z Z N B T H K A A Z H G')
print('O C I G H H N C O J R G W V M')
print('V Z N T Z H Z V J E U B C B T')
print()
scrtword = input('what is the secret number. you have 5 guesses (hint its a number not a word)')
if scrtword != "7":
   print('try again')
   print('you have 4 guesses left')
else:
    print('good job the number was 7')
print()
scrtword = input('what is the secret number (hint its numeric)')
if scrtword != "7":
   print('try again')
   print('you have 3 guesses left')
else:
    print('good job the number was 7')
print()
scrtword = input('what is the secret number (hint its numeric)')
if scrtword != "7":
   print('try again')
   print('you have 2 guesses left')
else:
    print('good job the number was 7')
print()
scrtword = input('what is the secret number (hint its numeric)')
if scrtword != "7":
   print('try again')
   print('you have 1 guesses left')
else:
    print('good job the number was 7')
print()
scrtword = input('what is the secret number (hint its numeric)')
if scrtword != "7":
   print('try again')
   print('you have 0 guesses left')
   print()
   print('YOU LOST')
else:
    print('good job the number was 7')