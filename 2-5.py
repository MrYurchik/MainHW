d1 = {'Ukraine': 'UA', 'Germany': 'DEU', 'Russia': 'RU', 'France': 'FRA', 'Belarus': 'BLR'}
d2 = {'UA': 'Kiev', 'DEU': 'Berlin', 'RU': 'Moscow', 'FRA': 'Paris',"BLR": 'Minsk'}
print(d1)
d1['Slovakia'] = 'SVK'
d2['SVK'] = 'Bratislava'
print(d1, d2)

def get_key(d1, value):
    for k, v in d1.items():
        if v == value:
            return k
x = (get_key(d1,'UA'))
print('Domain for', x, 'is', d1['Ukraine'])
