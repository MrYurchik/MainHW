name2 = 0
users = {
    'karas': 'karas',
    'arnold': 'arnold.',
    'bozdan': 'bozdan1.',
    'korchma': 'korchma1.'
}
name = input('Please enter your name: ')
name1 = name in users
if name1:
    pas1 = users[name]
    pas = input('Please enter your pass: ')
    if pas1 == pas:
        print("welldone")
    else:
        print("nea")
else:
    print('Bas nety B base')
