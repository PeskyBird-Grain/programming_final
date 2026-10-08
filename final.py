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

#puzzle room 1
number1 = random.randint(1,20)
number2 = random.randint(1,20)
number3 = random.randint(1,20)
correct = number1 * number2 
answer = input(int(f"What is {number1} * {number2}?\n"))
if answer == correct:
    print("Correct!")
else:
    print("Incorrect! Try again.")

    
#Upstairs:
#Room 1: 
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

#remy room dos: 
print('In the room you see a paper on a desk')
print('another child must have left it here')
print('???')
print('its a word search!?')
print()
print('D L L ')