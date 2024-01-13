import random

def generate_question():
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    return num1, num2

def check_answer(num1, num2, answer):
    return num1 * num2 == answer

def main():
    print("Welcome to the Multiplication Quiz!")
    print("Enter -1 to exit.")

    while True:
        num1, num2 = generate_question()
        user_answer = int(input(f"How much is {num1} times {num2}? "))

        if user_answer == -1:
            print("Thanks for playing. Goodbye!")
            break

        if check_answer(num1, num2, user_answer):
            print("Very good! Let's try another one.")
        else:
            print("No. Please try again.")

if __name__ == "__main__":
    main()
