from colorama import Fore, Back, Style

def example_a():
    print('\nExample A')
    print('~~~~~~~~~')

    print("Q: Have you ever farted in an elevator?")
    user_input = input("Enter \"y\" for yes or \"n\" for no: ")

    if user_input != "" and user_input is not None:
        if user_input.lower() == "y" or user_input.lower() == "yes":

            # Use colorama module to set the background color of the text
            # Style.RESET_ALL puts the console colors back to normal
            print(f"{Back.RED}Warning: This is Reeeeeeally important! {Style.RESET_ALL}")

            fart_victim_num = int(input("How many people were in the elevator? :"))

            # Python got the switch statement in v3.10
            match fart_victim_num:
                case x if x < 0:
                    print("Were they... Ghosts?")
                case 1:
                    print("Whoever that person was, they were disappointed in you...")
                case 2:
                    print("2 people? Well, everyone can blame each other.")
                case 3:
                    print(f"{fart_victim_num} people in the elevator, how could you?")
                case _:
                    # Default "catch-all" case
                    print(f"{fart_victim_num}!!! That's a target rich environment. Those poor people!")
        else:
            print("No? I don't believe you. Someone has probably done it to you though, right?")
    else:
        print("Error. You can't just enter blank space")


# Puzzle A - Workout of the day
# Write a program that provides a fitness exercise for the user to do, depending on what day of the week it is.
# Ask the user for the weekday.
#     "What day is it?: "
# Use a SWITCH statement to print out an exercise. The exercise should be different for each day.
# Make the console text a different COLOR for each day. NOT background color, make the text letter color different.
#      "Monday: 20 Sit ups"            (red text)
#      "Tuesday: 15 jumping jacks"     (blue text)
#      "Wednesday: 20 press ups"       (green text)
#      "Thursday: 10 burpees"          (yellow text)
#      ...
# Colorama documentation - https://pypi.org/project/colorama/
# Colorama github - https://github.com/tartley/colorama     (just for documentation, you do not need to install)
# Remember to convert the user's input to lowercase before comparison.
# Have a "default case" should the user not enter a weekday.
def puzzle_a():
    print('\nPuzzle A')
    print('~~~~~~~~~')

    user_input = input("What day is it?: ")

    if user_input != "" and user_input is not None:
        match user_input.lower():
            case "monday":
                print(f"{Fore.RED} Monday: 20 Sit ups {Style.RESET_ALL}")
            case "tuesday":
                print(f"{Fore.BLUE} Tuesday: 15 jumping jacks {Style.RESET_ALL}")
            case "wednesday":
                print(f"{Fore.GREEN} Wednesday: 20 press ups {Style.RESET_ALL}")
            case "thursday":
                print(f"{Fore.YELLOW} Thursday: 10 burpees {Style.RESET_ALL}")
            case "friday":
                print(f"{Fore.CYAN} Friday: 15min jog{Style.RESET_ALL}")
            case "saturday":
                print(f"{Fore.MAGENTA} Saturday: 20 barbell curls {Style.RESET_ALL}")
            case "sunday":
                print(f"{Fore.LIGHTRED_EX} Sunday: 15 min jog {Style.RESET_ALL}")
            case _:
                # Default runs only if they don't enter a day of the week
                print("20 bear crawls")

    else:
        print("Error. You can't just enter blank space")


def example_b():
    print('\nExample B')
    print('~~~~~~~~~')

    # Unicode / ANSI colors
    red = '\033[31m'
    blue = '\033[34m'
    green = '\033[32m'
    reset = '\033[0m'

    user_input = input("Choose a color: Red, Blue or Green: ")

    if user_input != "" and user_input is not None:

        # This preserves the original input variable, incase we need it later.
        user_input_lowercase = user_input.lower()

        if user_input_lowercase == "red" or user_input_lowercase == "r":
            print(f"{red} You chose Red... {reset} thanks!")
        elif user_input_lowercase == "blue" or user_input_lowercase == "b":
            print(f"{blue} You chose Blue... {reset} thanks!")
        elif user_input_lowercase == "green" or user_input_lowercase == "g":
            print(f"{green} You chose Green... {reset} thanks!")
        else:
            print("Sorry, no matching color...")
    else:
        print("Sorry, I did not understand...")


# Puzzle B - Color me in
# Re-write the above example program to use a SWITCH statement
# Use the unicode colors Cyan, Yellow and Magenta instead of red, blue and green.
# You might get confused with how to add "or" into the switch statement. Clue, it isn't "or".
# You should not need the null check for the switch as the default case should catch it.
def puzzle_b():
    print('\nPuzzle B')
    print('~~~~~~~~~')

    cyan = '\033[36m'
    yellow = '\033[33m'
    magenta = '\033[35m'
    reset = '\033[0m'

    user_input = input("Choose a color: Cyan, Yellow or Magenta: ")

    match user_input.lower():
        case "cyan" | "c":
            print(f"{cyan} You chose Cyan... {reset} thanks!")
        case "yellow" | "y":
            print(f"{yellow} You chose Yellow... {reset} thanks!")
        case "magenta" | "m":
            print(f"{magenta} You chose Magenta... {reset} thanks!")
        case _:
            print("Sorry, no matching color...")


def example_c():
    print('\nExample C')
    print('~~~~~~~~~~~')

    print("2 ? 5 = ?")
    print("Enter an operator and we will complete this sum...")
    user_input = input("Enter \"+\" or \"-\" :")

    match user_input:
        case "+":
            add_ans = 2 + 5
            print(f"2 + 5 = {add_ans}")
        case "-":
            minus_ans = 2 - 5
            print(f"2 - 5 = {minus_ans}")
        case _:
            print("Error, enter only + or - ")


# Puzzle C - Maths Switch
# Write a program using a switch statement, that allows the user to enter 2 numbers and choose the operator + - * /
# So the user could enter "2" then "*" then "7" in 3 separate input prompts.
# They will get the answer "2 * 7 = 14"
def puzzle_c():
    print('\nPuzzle C')
    print('~~~~~~~~~~~')

    num1 = int(input("Enter a number :"))

    operator_input = input("Enter \"+\" or \"-\" or \"*\" or \"/\":")

    num2 = int(input("Enter a second number :"))

    match operator_input:
        case "+":
            add_ans = num1 + num2
            print(f"{num1} + {num2} = {add_ans}")
        case "-":
            minus_ans = num1 - num2
            print(f"{num1} - {num2} = {minus_ans}")
        case "*":
            multiply_ans = num1 * num2
            print(f"{num1} * {num2} = {multiply_ans}")
        case "/":
            divide_ans = num1 / num2
            print(f"{num1} / {num2} = {divide_ans}")

            # You could also show remainder.
            divide_quotient = num1 // num2
            remainder = num1 % num2
            print(f"{num1} / {num2} = {divide_quotient} remainder {remainder}")
        case _:
            print("Error, enter only + or - or * or / ")


if __name__ == '__main__':

    # Run the puzzles

    example_a()
    #puzzle_a()

    example_b()
    #puzzle_b()

    example_c()
    #puzzle_c()

