import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4

#generates sequence user has to guess
def generate_code():
    code = []

    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
    return code


#Allows user to guess sequence
def guess_code():

    while True:
        guess = input("Guess: ").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"You must guess only {CODE_LENGTH} colors")
            continue #incorrect guess brings you back to top of while loop

        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again")
                break 
                #breaks me out of for loop to repeat while loop. If all colors valid pass onto else statement
        
        else:
            break #breaks me out of while loop
    
    return guess


def check_code(guess, real_code):
    color_counts = {} 
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1
    
    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1 #once all corr colors removed only incorrect pos colors left
    
    #only works once correct colors are removed by for loop above to prevent false positive incorrect pos
    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1
    
    return correct_pos, incorrect_pos

#main function links code together
def game():
    print(f"Welcome to Mastermind. You have {TRIES} attempts to guess the code...")
    print("The valid colors are", *COLORS)
    
    code = generate_code()

    for attempts in range(1, TRIES+1):
        guess = guess_code()
        correct_pos , incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code correctly in {attempts} tries ")
            break

        print(f"Correct Positions: {correct_pos}  |  Incorrect Positions: {incorrect_pos}")

    #else block runs if for loop doesn't terminate by break statement
    else:
        print("You ran out of tries, the code was:", *code) #asterisk makes it print nicer space-separated


if __name__ == "__main__":
    game()








