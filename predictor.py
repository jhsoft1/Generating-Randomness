import random
MINIMAL_LENGTH = 100
TRIADS =['000', '001', '010', '011', '100', '101', '110', '111']
dict_triads_0 = {}
dict_triads_1 = {}
for triad in TRIADS:
    dict_triads_0[triad] = dict_triads_1[triad] = 0
general_string = ''
len_gs = len(general_string)
print('Please give AI some data to learn...')
while len_gs < MINIMAL_LENGTH:
    print(f'The current data length is {len_gs}, {MINIMAL_LENGTH - len_gs} symbols left')
    user_input = input('Print a random string containing 0 or 1:\n\n')
    for char in user_input:
        if char in ['0', '1']:
            general_string += char
    len_gs = len(general_string)
print('\nFinal data string:')
print(general_string)
print()
for i in range(len_gs - 3):
    if general_string[i + 3] == '0':
        dict_triads_0[general_string[i: i+3]] += 1
    else:
        dict_triads_1[general_string[i: i+3]] += 1
# for triad in TRIADS:
    # print(f'{triad}: {dict_triads_0[triad]},{dict_triads_1[triad]}')
print('You have $1000. Every time the system successfully predicts your next press, you lose $1.')
print('Otherwise, you earn $1. Print "enough" to leave the game. Let\'s go!')
balance = 1000
while True:
    repeat = True
    while repeat:
        test_string = input('Print a random string containing 0 or 1:\n\n')
        if test_string == 'enough':
            print('Game over!')
            exit()
        repeat = False
        for char in test_string:
            if char not in ['0', '1']: repeat = True
    print('prediction:')
    prediction = ''
    for _ in range(3):
        prediction += str(random.choice('01'))
    guessed_right = 0
    for i in range(3, len(test_string)):
        if dict_triads_0[test_string[i-3: i]] > dict_triads_1[test_string[i-3: i]]:
            prediction += '0'
        else:
            prediction += '1'
        if prediction[i] == test_string[i]:
            guessed_right += 1
    print(prediction)
    max_right = len(test_string) - 3
    print(f'\nComputer guessed right {guessed_right} out of {max_right} symbols ({guessed_right/max_right*100:.2f} %)')
    balance += max_right - 2 * guessed_right
    print(f'Your balance is now ${balance}')
