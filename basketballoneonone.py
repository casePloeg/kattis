game = list(input())

a_points = 0
b_points = 0
for i in range(len(game)//2):
	player = game[i*2]
	points = int(game[i*2+1])
	if player == 'A':
		a_points += points
	elif player == 'B':	
		b_points += points

if a_points > b_points:
	print("A")
else:
	print("B")
