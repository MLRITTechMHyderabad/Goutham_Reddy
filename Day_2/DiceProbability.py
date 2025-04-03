import random

d1 = [1, 2, 3, 4, 5, 6]
d2 = [1, 2, 3, 4, 5, 6]
li = [(i, j) for i in d1 for j in d2]

dice = {}
for i in range(2, 13):
    c = sum(1 for j in li if i == j[0] + j[1])
    dice[str(i)] = c / 36

R = int(input("Enter the number of rounds: "))

plyr1_win = 0
plyr2_win = 0

for _ in range(R):
    p1_d1, p1_d2 = random.randint(1, 6), random.randint(1, 6)
    p2_d1, p2_d2 = random.randint(1, 6), random.randint(1, 6)

    p1_sum = p1_d1 + p1_d2
    p2_sum = p2_d1 + p2_d2

    p1_probability = dice[str(p1_sum)]
    p2_probability = dice[str(p2_sum)]

    if p1_probability < p2_probability:
        plyr1_win += 1
    elif p2_probability < p1_probability:
        plyr2_win += 1

if plyr1_win > plyr2_win:
    print("Player 1 wins")
elif plyr1_win < plyr2_win:
    print("Player 2 wins")
else:
    print("It's a tie")
