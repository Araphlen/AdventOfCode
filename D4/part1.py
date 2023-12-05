f= open("D4\input.txt","r")
lines = f.readlines()

tot_points=0

for line in lines:
    cardpoints = 0
    parts = line.split(":")
    cardslists = parts[1].split("|")
    winning_cards = cardslists[0].split()
    my_cards = cardslists[1].split()
    for number in my_cards:
        if number in winning_cards:
            if cardpoints>0:
                cardpoints*=2
            else:
                cardpoints=1
    tot_points+=cardpoints

print(tot_points)