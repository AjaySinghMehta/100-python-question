while True:
    name = input('enter your name : ')
    if name != 'ajay':
        continue
    password = input('enter the password : ')
    if password == "mehta":
        break
    print('wrong password')
print('welcome out of the loop :>')