import random

alreadyDealt = []

deck = {}
deckValues = {}


def setDeckValues():
    for idx, card in deck.items():
        if "Ace" in card:
            deckValues[card] = 11
        if "King" in card or "Queen" in card or "Jack" in card or "Ten" in card:
            deckValues[card] = 10
        if "Nine" in card:
            deckValues[card] = 9
        if "Eight" in card:
            deckValues[card] = 8
        if "Seven" in card:
            deckValues[card] = 7
        if "Six" in card:
            deckValues[card] = 6
        if "Five" in card:
            deckValues[card] = 5
        if "Four" in card:
            deckValues[card] = 4
        if "Three" in card:
            deckValues[card] = 3
        if "Two" in card:
            deckValues[card] = 2


def makeDeck():
    suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
    cards = ["Ace", "King", "Queen", "Jack", "Ten", "Nine", "Eight",
             "Seven", "Six", "Five", "Four", "Three", "Two"]
    i = 1
    for card in cards:
        for suit in suits:
            deck[i] = card + " of " + suit
            i += 1
    setDeckValues()


def menu():
    while 1:
        startGame = input("Ready to play? (Y/N): ")
        if startGame.lower() == "y":
            print("Let's play!")
            game()
            break
        elif startGame.lower() == "n":
            while 1:
                quit = input("Do you want to quit? (Y/N): ")
                if quit.lower() == "y":
                    print("Ok, Bye!")
                    exit(0)
                elif quit.lower() == "n":
                    print("Ok. I'll wait")
                    break
                else:
                    print("I didn't understand your input.")
        else:
            print("I didn't understand your input.")


def game(moneyPot=1000, sim=0):
    if moneyPot == 0:
        print("You are out of money. Game over :(")
        exit(0)
    print("You have $" + str(moneyPot) + " in your pot.")
    while 1:
        print("How much do you want to bet?")
        bet = input("Enter a number less than or equal to " +
                    str(moneyPot) + ": ")
        try:
            val = int(bet)
        except ValueError:
            print("You must enter a number!")
            continue
        if val > moneyPot:
            print("You don't have enough money! Try again!")
            continue
        if val < 0:
            print("You must enter a positive number.")
            continue
        break

    print("Dealing...")
    dealersCards = deal()
    yourCards = deal()
    showCards(yourCards, dealersCards)
    total = calculateHand(yourCards)
    if total > 21:
        print("BUST! Dealer Wins! :(")
        moneyPot -= val
        while 1:
            playAgain = input("Play again? (Y/N) ")
            if playAgain.lower() == "y":
                game(moneyPot)
            elif playAgain.lower() == "n":
                print("Ok. You're leaving with $" + str(moneyPot))
                print("Bye!")
                exit(0)
            else:
                print("I didn't understand your input.")
    while 1:
        hitInput = input("Hit (1)? or Stay (2)? ")
        if hitInput == '1':
            newCard = hit()
            yourCards.append(newCard)
            showCards(yourCards, dealersCards)
            total = calculateHand(yourCards)
            if total > 21:
                moneyPot -= val
                print("BUST! Dealer Wins! :(")
                while 1:
                    playAgain = input("Play again? (Y/N) ")
                    if playAgain.lower() == "y":
                        game(moneyPot)
                    elif playAgain.lower() == "n":
                        print("Ok. You're leaving with $" + str(moneyPot))
                        print("Bye!")
                        exit(0)
                    else:
                        print("I didn't understand your input.")
        elif hitInput == '2':
            stay(yourCards, dealersCards, moneyPot, val)
        else:
            print("I didn't understand your input.")
            print("Enter 1 to Hit or 2 to Stay.")


def showCards(yourCards, dealersCards, stay=False):
    print()
    print()
    print("Dealer's Cards:")
    dealerStr = ""
    print("[ X ] [" + dealersCards[1] + "]")
    if stay:
        for card in dealersCards:
            dealerStr += "[" + card + "] "
        dealerStr += "(" + str(calculateHand(dealersCards)) + ")"
    print(dealerStr)
    print()
    print()
    print("Your Cards: ")
    cardsStr = ""
    for card in yourCards:
        cardsStr += "[" + card + "] "
    cardsStr += "(" + str(calculateHand(yourCards)) + ")"
    print(cardsStr)
    print()
    print()


def deal():
    global alreadyDealt
    alreadyDealt = []
    print(alreadyDealt)
    rand1 = random.randint(1, 52)
    while rand1 in alreadyDealt:
        rand1 = random.randint(1, 52)
    alreadyDealt.append(rand1)
    rand2 = random.randint(1, 52)
    while rand2 in alreadyDealt:
        rand2 = random.randint(1, 52)
    alreadyDealt.append(rand2)
    return [deck[rand1], deck[rand2]]


def hit():
    rand = random.randint(1, 52)
    while rand in alreadyDealt:
        rand = random.randint(1, 52)
    alreadyDealt.append(rand)
    return deck[rand]


def stay(yourCards, dealersCards, moneyPot, bet):
    yourTotal = calculateHand(yourCards)
    dealerTotal = calculateHand(dealersCards)
    if dealerTotal > yourTotal:
        showCards(yourCards, dealersCards, stay=True)
        print("You lose :(")
        moneyPot -= bet
        while 1:
            again = input("Play again? (Y/N) ")
            if again.lower() == "y":
                game(moneyPot)
            elif again.lower() == "n":
                print("Ok. You're leaving with $" + str(moneyPot))
                print("Bye!")
                exit(0)
            else:
                print("I didn't understand your input.")
    while dealerTotal < 21:
        print("Dealer is drawing...")
        dealersCards.append(hit())
        showCards(yourCards, dealersCards, stay=True)
        dealerTotal = calculateHand(dealersCards)
        if dealerTotal > 21:
            print("You win!")
            moneyPot += bet
            while 1:
                again = input("Play again? (Y/N) ")
                if again.lower() == "y":
                    game(moneyPot)
                elif again.lower() == "n":
                    print("Ok. You're leaving with $" + str(moneyPot))
                    print("Bye!")
                    exit(0)
                else:
                    print("I didn't understand your input.")
        elif dealerTotal > yourTotal:
            print("You lose :(")
            moneyPot -= bet
            while 1:
                again = input("Play again? (Y/N) ")
                if again.lower() == "y":
                    game(moneyPot)
                elif again.lower() == "n":
                    print("Ok. You're leaving with $" + str(moneyPot))
                    print("Bye!")
                    exit(0)
                else:
                    print("I didn't understand your input.")


def calculateHand(hand):
    total = 0
    for card in hand:
        total += deckValues[card]
    if total > 21:
        if "Ace" in str(hand):
            total -= 10
    return total


print("Welcome to the blackjack simulator!")
makeDeck()
menu()
