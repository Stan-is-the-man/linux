a = [1, 2, 3, 4, 5, 6, 7]
b = [num for num in a if num % 2 == 0]
print(b)
#############################
word = ' I love SQL'
print(word[:: -1])

text = 'I love SQL'
word = text.split(' ')
rev = []

for _ in range(len(word)):
    rev.append(word.pop())

print(' '.join(rev))

############################
from collections import deque

people = deque()

while True:
    command = input()
    if command == 'End':
        print(people)
        break
    elif command == 'Paid':
        while len(people):
            print(f'Customer {people.popleft()} has been paid')
    else:
        people.append(command)
#################################
from collections import deque

sequence = deque()
n = int(input())

for _ in range(n):
    command = input()
    if " " in command:
        number = command.split(" ")[1]
        sequence.append(number)
    elif command == '2' and len(sequence):
        sequence.pop()
    elif command == '3' and len(sequence) :
        print(max(sequence))
    elif command == '4' and len(sequence):
        print(min(sequence))

rev = reversed(sequence)
print(', '.join(rev))

################################
# dict compr:
a = [('amy',23), ('gosho', 30)]

dict_compr = {key:value for key, value in a}
print(dict_compr)
#########################
a = [1, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, ]

b = set(a)
c = {num for num in a}
print(b,c)
###############
matrix = [[j for j in range(5)]for i in range(10)]
print(matrix)
#############
x = lambda a: a ** a

print(x(78))
############
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(4))
###############33

