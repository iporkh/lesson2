string1 = input('Напишите что-нибудь: ')
string2 = input('И еще что-нибудь ')

if len(string1) == len(string2):
	print('1')

elif len(string1) > len(string2):
	print('2')

elif not string1.lower() == string2.lower():
	if string2 == 'learn':
		print('3')