print('Welcome to asl python Quiz')

answer = input('Are you ready to play the quiz? (yes/no):')
score = 0
total_questions = 3

if answer.lower() == 'yes':
    answer = input('Question 1:What is your favourite programming language')
    if answer.lower() == 'python':
        score += 1
        print('correct')
    else:
        print('Wrong Answer:(')

    answer = input('Question 2:Do you follow any author on AskPython?')
    if answer.lower() == 'yes':
        score += 1
        print('Correct')
    else:
        print('Wrong Answer :(')

    answer = input('Question 3:What is the name of your favourite website for learning python? ')
    if answer.lower() == 'askPython':
        score += 1
        print('correct')
    else:
        print('Wrong Answer:(')


print('Thank you for playing this small quiz game ,you attempted',score ,'questions correctly')
