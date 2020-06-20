import random
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suits = ['C', 'D', 'H', 'S']
cards = [[rank, suit] for rank in ranks for suit in suits]
random.shuffle(cards)
human = cards[0:5]
bot = cards[26:31]
pot = []
print(f"""
bot   : {bot}
human : {human}
pot   : {pot}
""")
Number_of_cards_drew = 0
turn = True
while True:
    command = input("What would you like to do ").lower()
    if command == "draw" :
        if turn == False:
            bluff = input("You already drew the cards. Enter the suit that you want to go in with ").upper()
            print(f"""I have {Number_of_cards_drew} {bluff}(s) on the table""")
            break
        while True:
            print(human)
            index = int(input("Enter a card index or simply input 0 if you're done  "))
            if index != 0 and index<len(human) :
                pot.append(human[index - 1])
                human.remove(human[index - 1])
                Number_of_cards_drew += 1
                turn = False
            else :
                break
    elif command == "quit":
        break
    else :
        print("i don't understand !")
