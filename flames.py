#Simples Flames program

def flames_predictor(name1, name2):

	name1 = name1.replace(' ', '').lower()
	name2 = name2.replace(' ', '').lower()

	for i in name1.strip().lower():
		for j in name2.lower():
			if i == j:
				name1 = name1.replace(i, '')
				name2 = name2.replace(j, '')

	count = len(name1) + len(name2)

	flames = ['f', 'l', 'a', 'm', 'e', 's']

	if count == 0:
		return print('No compatibility. Names have the same letters')

	while len(flames) > 1:
		
		cut_index = count - len(flames)
		cut_index = cut_index - 1
		
		while cut_index > len(flames)-1:
			cut_index = cut_index - len(flames)

		flames.pop(cut_index)

	flames_dict = {'f': 'friend', 'l': 'love', 'a': 'affection', 'm': 'marriage', 'e': 'enemy', 's':'sister'}

	return print('According to Flames games, compatibility between you and your partner is ', flames_dict[flames[0]].upper())

name1 = input('Enter your name: ')
name2 = input('Enter your partner\'s name: ')

flames_predictor(name1, name2)