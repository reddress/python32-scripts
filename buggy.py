import random
n1 = random.randint(1, 10)
n2 = random.randint(1, 10)
print('What is ' + str(n1) + ' + ' + str(n2) + '?')
answer = input()
if int(answer) == n1 + n2:
    print('Correct')
else:
    print('Nope the answer is ' + str(n1 + n2))
    
