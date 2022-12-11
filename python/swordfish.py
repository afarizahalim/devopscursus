while True:
    name = input('Who are you? ')
    if name != 'Joe':
        continue
    password = input(f'Hello {name}. What is the password: ')
    if password == 'swordfish':
        break
print('Access granted')