problem = input('Enter a math problem,or "q" to quit: ')
while 'q' != problem:
    print('The answer to ', problem, ' is:', eval(problem))
    problem = input('Enter another math problem, or "q" to quit: ')