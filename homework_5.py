my_list = ["apple", 'orange', 'peach', 'melon', 'mango']
print (f'List:{my_list}')
print(f'First & last elements: {my_list[0:5:4]}')
print(f'Sublist: {my_list[2:6]}')
my_list[2] = 'redbomb'
print(f'Modified list: {my_list}')

my_dict = {
    "white" : 'белый',
    'green' : 'зеленый',
    'yellow' : 'желтый',
    'blue' : 'синий',
    'red' : 'красный',
}
print(f'Dictionary: {my_dict}')
print(f'Translation: {my_dict['green']}')
my_dict['blue'] = 'голубой'
my_dict['black'] = 'черный'
print(f'Modified dictionary: {my_dict}')