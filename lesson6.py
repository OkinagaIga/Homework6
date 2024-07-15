my_dict = {'Alohomora': 'Unlocking Charm', 'Wingardium Leviosa': 'Levitation Charm', 'Avada Kedavra': 'Killing Curse', 'Expecto Patronum': 'Patronus Charm'}
print(my_dict)
print(my_dict['Alohomora'])
my_dict['Riddikulus'] = 'Boggart Banishing Spell'
print(my_dict['Riddikulus'])
my_dict.update({'Accio': 'Summoning Charm',
                'Legilimens': 'Legilimency Spell'})
print(my_dict.pop('Avada Kedavra'))
print(my_dict)

my_set = {'Alohomora', 1, 1, 2, 4, 'Alohomora', False, 'Alohomora', 4}
print(my_set)
print(my_set.add('Riddikulus'))
print(my_set.add(8))
print(my_set.discard(1))
print(my_set)