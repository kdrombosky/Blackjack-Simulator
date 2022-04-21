import random

alreadyDealt = []

deck = {}
deckValues = {}
faceCards = {"Ace", "King", "Queen", "Jack", "Ten"}


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


def calculateHand(hand):
    total = 0
    for card in hand:
        total += deckValues[card]
    if total > 21:
        if "Ace" in str(hand):
            total -= 10
    return total


def sim3(moneyPot=1000, rounds=0, highestPot=1000):
    rounds += 1
    print("Round " + str(rounds))
    if moneyPot > highestPot:
        highestPot = moneyPot
    if moneyPot <= 0:
        print("You are out of money. Game over :(")
        print("Highest amount of money: $" + str(highestPot))
        print("Rounds: " + str(rounds))
        exit(0)
    bet = 100

    print("Dealing...")
    dealersCards = deal()
    yourCards = deal()
    showCards(yourCards, dealersCards)
    total = calculateHand(yourCards)
    if total > 21:
        print("BUST! Dealer Wins! :(")
        moneyPot -= bet
        sim3(moneyPot, rounds, highestPot)
    while 1:
        face = False
        for card in yourCards:
            for faceC in faceCards:
                if faceC in card:
                    face = True
        if not face:
            newCard = hit()
            yourCards.append(newCard)
            showCards(yourCards, dealersCards)
            total = calculateHand(yourCards)
            if total > 21:
                moneyPot -= bet
                print("BUST! Dealer Wins! :(")
                sim3(moneyPot, rounds, highestPot)
        else:
            print("A face card is present. Staying...")
            simStay(yourCards, dealersCards, moneyPot, bet, rounds, highestPot)


def simStay(yourCards, dealersCards, moneyPot, bet, rounds, highestPot):
    yourTotal = calculateHand(yourCards)
    dealerTotal = calculateHand(dealersCards)
    if dealerTotal == yourTotal:
        showCards(yourCards, dealersCards, stay=True)
        print("You tied the dealer!")
        sim3(moneyPot, rounds, highestPot)

    if dealerTotal > yourTotal:
        showCards(yourCards, dealersCards, stay=True)
        print("You lose :(")
        moneyPot -= bet
        sim3(moneyPot, rounds, highestPot)

    while dealerTotal < 21:
        print("Dealer is drawing...")
        dealersCards.append(hit())
        showCards(yourCards, dealersCards, stay=True)
        dealerTotal = calculateHand(dealersCards)
        if dealerTotal > 21:
            print("You win!")
            moneyPot += bet
            sim3(moneyPot, rounds, highestPot)

        elif dealerTotal > yourTotal:
            print("You lose :(")
            moneyPot -= bet
            sim3(moneyPot, rounds, highestPot)


print("Black Jack Simulation 3: ")
print("Always stay when you have a face card/Straight Betting")
highestPot = 1000
makeDeck()
sim3()
