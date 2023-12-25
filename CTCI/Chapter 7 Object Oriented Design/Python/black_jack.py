from enum import Enum
from typing import List
import random

class Suit(Enum):
    DIAMONDS = 0
    HEARTS = 1
    CLUBS = 2
    SPADES = 3

class Card:
    def __init__(self, val: int, suit: Suit):
        self._val = val
        self._suit = suit

        self._face_val_map = {
            11: 'A',
            12: 'K',
            13: 'Q',
            14: 'J'
        }

    @property
    def value(self):
        return self._val

    @value.setter
    def value(self, val: int):
        self._val = val

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, suit: Suit):
        self.suit = suit

    def get_face(self):
        return self._face_val_map.get(self._val, str(self._val))

    def __repr__(self):
        return f"{self.get_face(self._val)} of {self._suit.name}"

    def _is_face_card(self):
        return self.get_face() in ['K', 'Q', 'J']

    def get_score(self) -> int:
        if self._is_face_card():
            return 10
        return self._val

class Deck:
    def __init__(self):
        self.cards = []
        
        for i in range(4):
            for card in self._create_cards(13, i):
                self.cards.append(card)

        self.shuffle_deck()

    def _create_cards(self, num: int, suit: int) -> List[Card]:
        for val in range(2, num + 2):
            yield Card(val, Suit(suit))

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def display_all(self):
        for card in self.cards:
            print(card)
        
    def deal(self):
        if not self.cards:
            raise OutOfCardsException
        return self.cards.pop()

class BlackjackHand:
    def __init__(self, card1: Card, card2: Card):
        self._cards = [card1, card2]
        self._score = 0
        self._update_score(card1)
        self._update_score(card2)

    def _update_score(self, card):
        if card.get_face() == 'A':
            if self._score < 21: self._score += 11
            else: self._score += 1
        else: self._score += card.get_score()

    def add(self, card: Card) -> None:
        self._cards.append(card)
        self._update_score(card)

    def get_score(self) -> int:
        return self._score

    def display_score(self):
        print(f"Current Score: {self._score}")

    def is_21(self) -> bool:
        return self._score == 21

class OutOfCardsException(Exception):
    pass

if __name__ == '__main__':
    deck = Deck()
    blackjack_hand = BlackjackHand(deck.deal(), deck.deal())

    while blackjack_hand.get_score() < 21:
        blackjack_hand.display_score()
        blackjack_hand.add(deck.deal())

    if blackjack_hand.is_21():
        print('Blackjack!!')
    else:
        blackjack_hand.display_score()
        print('Busted.')