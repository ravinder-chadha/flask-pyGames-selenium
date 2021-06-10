from questions import QUESTIONS

def isAnswerCorrect(question, answer):

    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''

    return True if answer == question['answer'] else False      #remove this


def lifeLine(i):

    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''
    from random import choice
    print(f'\tQuestion{i+1}:{QUESTIONS[i]["name"]}')
    print(f'\t\tOptions:')
    correct=QUESTIONS[i]['answer']
    print(f"\t\t\tOption {correct}:{QUESTIONS[i]['option'+str(correct)]}")
    a=[1,2,3,4]
    a.remove(correct)
    x=choice(a)
    print(f"\t\t\tOption {x}:{QUESTIONS[i]['option'+str(x)]}")


def kbc():
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''

    #  Display a welcome message only once to the user at the start of the game.
    #  For each question, display the prize won until now and available life line.
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks
    end_of_game=True
    lifeLineAvailable=True
    i=0
    while end_of_game:
        print(f'\tQuestion {i+1}: {QUESTIONS[i]["name"]}' )
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[i]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[i]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[i]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[i]["option4"]}')
        ans = input('Your choice ( 1-4 ) : ')
        if ans.lower()=='quit':
            end_of_game=False
        elif ans.lower()=='lifeline':
            if lifeLineAvailable:
                lifeLineAvailable=False
                lifeLine(i)
                ans = input('Your choice : ')
                isAnswerCorrect(QUESTIONS[i], int(ans) )
                # print the total money won.
                print(f"You have won {QUESTIONS[i]['money']}")
                # See if the user has crossed a level, print that if yes
                print('\nCorrect !')
                i+=1
            else:
                print("lifeline is not available")
        # check for the input validations
        # elif not lifeLineAvailable and ans.lower=='lifeline':
        #     print("Lifeline is not available")
        #     continue

        elif isAnswerCorrect(QUESTIONS[i], int(ans) ):
            # print the total money won.
            print(f"You have won {QUESTIONS[i]['money']}")
            # See if the user has crossed a level, print that if yes
            print('\nCorrect !')
            i+=1

        else:
            # end the game now.
            # also print the correct answer
            print('\nIncorrect !')
            print(f"Correct answer is:{QUESTIONS[i]['answer']}")
            end_of_game=False

    # print the total money won in the end.
    print(f"You have won {QUESTIONS[i]['money']}")


kbc()
