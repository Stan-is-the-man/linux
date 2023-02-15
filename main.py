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
