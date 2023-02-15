a = [1, 2, 3, 4, 5, 6, 7]
b = [num for num in a if num % 2 == 0]
print(b)

word = ' I love SQL'
print(word[:: -1])

text = 'I love SQL'
word = text.split(' ')
rev = []

for _ in range(len(word)):
    rev.append(word.pop())

print(' '.join(rev))


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

