import random
def guess(x):
    random_number = random.randint(1,x)
    guess1 = 0
    while(guess1!=random_number):
        guess1 = int(input("Enter any number: "))
        if guess1>random_number:
            print('Sorry you guessed a higher number')
        elif guess1<random_number:
            print('Sorry you have guessed a lower number')

    print(f'congrats! you have guessed the correct number.The number is {random_number}')

def computer_guess(x):
    low = 1
    high = x
    feedback=''
    while feedback !='c' and low != high:
        if low!=high:
            guess1 = random.randint(low,high)
        else:
            guess = low
        feedback=input(f'Is {guess1} too high (H),too low (L) or correct (C)??').lower()
        if feedback == 'h':
            high = guess1 - 1
        elif feedback == 'l':
            low = guess1 + 1

    print(f'Yay!! The computer guessed your number,{guess1}, correctly!')
computer_guess(1000)