import csv

score = 0
line_count = 0
applied_ques = 0

# Initialize a dictionary
options = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4
}

def check_guess(guess, answer):
    global score, applied_ques
    if guess == answer:
        print('Correct answer!')
        score += 1
    else:
        print(f'Wrong!, The answer is: {answer}')
    applied_ques += 1

def show_score():
    print(f'Total Score: {score}/{applied_ques}.')


if __name__ == "__main__":
    print('========== World Quiz ==========')

    with open('questions.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)

        for row in csvreader:
            if line_count == 0:
                line_count += 1
            else:
                print(f"{row[0]}\nA.{row[1]} \nB.{row[2]} \nC.{row[3]} \nD.{row[4]}\n")
                correct_choice = False
                
                while not correct_choice:
                    guess = input("Type A, B, C, or D : ")
                    if guess.upper() in ['A', 'B', 'C', 'D']:
                        check_guess(row[options[guess.upper()]], row[5])
                        correct_choice = True
                    
                line_count += 1
                print("\n")

                if applied_ques == 10:
                    show_score()
                    play_again = input('Want to play again?(Y/N): ')
                    if play_again in ['N', 'n']:
                        break
                    else:
                        line_count = 1
                        applied_ques = 0
                        score = 0
        if applied_ques != 10:
            show_score()

        print('Thanks for Playing! Goodbye')