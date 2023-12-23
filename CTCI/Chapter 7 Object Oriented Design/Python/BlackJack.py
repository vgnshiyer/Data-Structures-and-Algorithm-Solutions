import random

class Card:
    def __init__(self, suit : str, val : str):
        if suit == 0:
            self.suit = 'Hearts'
        elif suit == 1:
            self.suit = 'Diamonds'
        elif suit == 2:
            self.suit = 'Spades'
        else:
            self.suit = 'Clubs'
        
        if val == 11:
            self.val = 'Ace'
        elif val == 12:
            self.val = 'King'
        elif val == 13:
            self.val = 'Queen'
        elif val == 14:
            self.val = 'Jack'
        else:
            self.val = str(val)

    def describe(self):
        print('{0} of {1}'.format(self.getValue(), self.getSuit()))

    def getValue(self) -> str:
        return self.val

    def getBlackJackValue(self) -> int:
        if self.val == 'Ace': return 1
        if self.val in ['King', 'Queen', 'Jack']: return 10
        return int(self.val)

    def getSuit(self) -> str:
        return self.suit

class Hand:
    cards = []
    handScore = -1

    def score(self) -> int:
        score = 0
        for card in self.cards:
            if card.getValue() == 'Ace': ## 1 or 11
                if score > 21:
                    score += 1
                else:
                    score += 11
            else:
                score += card.getBlackJackValue()
        self.handScore = score
        return score

    def add(self, card: Card):
        self.cards.append(card)
        self.score()

    def is21(self) -> bool:
        return self.handScore == 21

    def isBusted(self) -> bool:
        return self.handScore > 21

class Deck:
    __deck = []
    k = 0

    def __init__(self):
        for i in range(52):
            suit = i//13
            val = i%13 + 2
            self.__deck.append(Card(suit, val))

        self.shuffle()

    def printDeck(self):
        for card in self.__deck:
            card.describe()

    def shuffle(self):
        random.shuffle(self.__deck)

    def deal(self) -> Card:
        if self.k >= 52: 
            raise Exception('Out of cards. Deck is empty!!')
        card = self.__deck[self.k]
        self.k += 1
        return card 

if __name__ == '__main__':
    deck = Deck()
    hand = Hand()

    card1 = deck.deal()
    hand.add(card1)
    card2 = deck.deal()
    hand.add(card2)

    while(hand.score() < 21):
        print('Current score: {0}'.format(hand.score()))
        hand.add(deck.deal())

    if hand.is21():
        print('Blackjack!!')
    else:
        print('Current score: {0}'.format(hand.score()))
        print('Busted.')