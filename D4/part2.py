f= open("D4\input.txt","r")
lines = f.readlines()

tot_scratchcards=0
cards_copy_nb = [1 for i in range(len(lines))]

def get_card_nubmers(i_card):
    parts = lines[i_card].split(":")
    cardslists = parts[1].split("|")
    winning_cards = cardslists[0].split()
    my_cards = cardslists[1].split()
    return winning_cards,my_cards

def get_nb_copies_from_card(i_card):
    my_cards,winning_cards= get_card_nubmers(i_card)
    nb_matchs=0

    for number in my_cards:
        if number in winning_cards:
            nb_matchs+=1
    for i in range(1,nb_matchs+1):
        if i_card+i<len(lines):
            cards_copy_nb[i_card+i]+=1*cards_copy_nb[i_card]

for i_card in range(len(lines)):
    get_nb_copies_from_card(i_card)

print(cards_copy_nb)
for nb in cards_copy_nb:
    tot_scratchcards+=nb

print(tot_scratchcards)