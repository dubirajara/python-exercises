import random


jokenpo = ['rock', 'paper', 'scissors']
random.shuffle(jokenpo)

def select():
	print('\nSelect: "Rock, Paper or Scissors"')
	player = input('> ').lower()
	enemy = random.choice(jokenpo)

	if player in jokenpo:

		if player == enemy:
			print('\nDraw!!!')

		elif player == 'rock' and enemy == 'scissors':
			print('\nYou Win, {0} breaks {1}'.format(player, enemy))

		elif player == 'paper' and enemy == 'rock':
			print('\nYou Win, {0} covers {1}'.format(player, enemy))

		elif player == 'scissors' and enemy == 'paper':
			print('\nYou Win, {0} cuts {1}'.format(player, enemy))

		else:
			print('\nYou lose!!! you: {0} and the machine win: {1}'.format(player, enemy))
		
		try_again()

	else:
		select()


def try_again():
	a = input("\nDo you want to keep playing y/n ? ")

	while a.lower() != 'y' and a.lower() != 'n':
		a = input("\nDo you want to keep playing y/n ? ")

	if a.lower() == ("y"):
		select()

	else:
		print("\nGame Over!!!")


        
select()




