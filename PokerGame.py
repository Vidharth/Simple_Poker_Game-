# coding=utf-8
import random
import itertools

print("Welcome to Poker Game!")
print("♣ ♦ ♥ ♠")


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def return_card(self):
        return "{}_{}".format(self.value, self.suit)


class Deck:
    def __init__(self):
        self.cards = []

    def build_deck(self):
        for suit in ["♣", "♦", "♥", "♠"]:
            for value in range(2, 15):
                if value == 11:
                    value = "J"
                elif value == 12:
                    value = "Q"
                elif value == 13:
                    value = "K"
                elif value == 14:
                    value = "A"
                self.cards.append(Card(value, suit))

    def shuffle_deck(self):
        for _ in range(0, len(self.cards)):
            random_card = random.randint(0, len(self.cards) - 1)
            self.cards[_], self.cards[random_card] = self.cards[random_card], self.cards[_]

    def return_deck(self):
        return_deck = []
        for _ in self.cards:
            return_deck.append(_.return_card())
        return return_deck


class Player:
    def __init__(self):
        self.hand = []

    def draw_hand(self, _):
        self.hand.append(_.pop())

    def return_hand(self):
        return_hand = []
        for _ in self.hand:
            return_hand.append(_)
        return return_hand


class Poker:

    def high_card(self, _):
        # check and fix equal cards, also implement second highest card
        rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        value = []
        card_rank = []
        for item in _:
            value.append(item.split("_")[0])
        value1, value2 = value[0], value[1]
        for position, item in enumerate(rank):
            if item == value1:
                card_rank.append((position, value1))
            elif item == value2:
                card_rank.append((position, value2))
        if card_rank[0][0] >= card_rank[1][0]:
            return card_rank[0][1]
        else:
            return card_rank[1][1]

    def flush(self, _):
        suit = []
        for _ in _:
            suit.append(_.split("_")[1])
        club = "♣"
        diamond = "♦"
        heart = "♥"
        spade = "♠"
        cflush = True
        dflush = True
        hflush = True
        sflush = True
        win = "FLUSH!"
        for item in suit:
            if club != item:
                cflush = False
                break
        for item in suit:
            if diamond != item:
                dflush = False
                break
        for item in suit:
            if heart != item:
                hflush = False
                break
        for item in suit:
            if spade != item:
                sflush = False
                break
        if cflush:
            return suit
        elif dflush:
            return suit
        elif hflush:
            return suit
        elif sflush:
            return suit
        else:
            return suit

    def pair_two_pair(self, _):
        value = []
        for _ in _:
            value.append(_.split("_")[0])
        player_cards = [value[0], value[1]]
        community_cards = [value[2], value[3], value[4]]
        new_value = []
        for value1 in player_cards:
            for value2 in community_cards:
                new_value.append((value1, value2))
        new_value.append(player_cards)
        pair = []
        for item in new_value:
            if item[0] == item[1]:
                pair.append((item[0], item[1]))
        return pair

    def triplet(self, _):
        value = []
        for _ in _:
            value.append(_.split("_")[0])
        new_value = []
        for value1, value2, value3 in itertools.combinations(value, 3):
            new_value.append((value1, value2, value3))
        triplet = []
        for item in new_value:
            if item[0] == item[1] and item[1] == item[2]:
                triplet.append((item[0], item[1], item[2]))
        return triplet

    def four_of_a_kind(self, _):
        value = []
        for _ in _:
            value.append(_.split("_")[0])
        new_value = []
        for value1, value2, value3, value4 in itertools.combinations(value, 4):
            new_value.append((value1, value2, value3, value4))
        four_of_a_kind = []
        for item in new_value:
            if item[0] == item[1] and item[1] == item[2] and item[2] == item[3]:
                four_of_a_kind.append((item[0], item[1], item[2], item[3]))
        return four_of_a_kind

    def full_house(self, _):
        pair_two_pair(self, _)
        triplet(self, _)

    def straight(self, _):
        value = []
        for _ in _:
            value.append(_.split("_")[0])
        # check and make an exception for Ace
        rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        card_position = []
        card_value = []
        for position, item in enumerate(rank):
            if item in value:
                card_position.append(position)
                card_value.append(item)
        groups = []
        value1 = value2 = card_position[0]
        for _ in card_position[1:]:
            if _ == value2 + 1:
                value2 = _
            else:
                groups.append(value1 if value1 == value2 else (value1, value2))
                value1 = value2 = _
        groups.append(value1 if value1 == value2 else (value1, value2))
        if len(groups) == 1:
            return card_value
        else:
            return card_value

    def straight_flush(self, _):
        straight(self, _)
        flush(self, _)

    def royal_flush(self, _):
        flush(self, _)


def test():
    card = Card(10, "♠")
    my_card = card.return_card()
    print(my_card)
    deck = Deck()
    deck.build_deck()
    straight_deck = deck.return_deck()
    print(straight_deck)
    deck.shuffle_deck()
    deck.shuffle_deck()
    shuffle_deck = deck.return_deck()
    print(shuffle_deck)
    player1 = Player()
    player1.draw_hand(shuffle_deck)
    player1.draw_hand(shuffle_deck)
    player1_hand = player1.return_hand()
    print(player1_hand)
    player2 = Player()
    player2.draw_hand(shuffle_deck)
    player2.draw_hand(shuffle_deck)
    player2_hand = player2.return_hand()
    print(player2_hand)
    community_cards = Player()
    community_cards.draw_hand(shuffle_deck)
    community_cards.draw_hand(shuffle_deck)
    community_cards.draw_hand(shuffle_deck)
    community_cards_hand = community_cards.return_hand()
    print(community_cards_hand)
    player1_hand = player1_hand + community_cards_hand
    print(player1_hand)
    player2_hand = player2_hand + community_cards_hand
    print(player2_hand)
    print(shuffle_deck)
    win_condition = Poker()
    high_card1 = win_condition.high_card(player1_hand)
    print(high_card1)
    high_card2 = win_condition.high_card(player2_hand)
    print(high_card2)
    flush1 = win_condition.flush(player1_hand)
    print(flush1)
    flush2 = win_condition.flush(player2_hand)
    print(flush2)
    pair1 = win_condition.pair_two_pair(player1_hand)
    print(pair1)
    pair2 = win_condition.pair_two_pair(player2_hand)
    print(pair2)
    triplet1 = win_condition.triplet(player1_hand)
    print(triplet1)
    triplet2 = win_condition.triplet(player2_hand)
    print(triplet2)
    four_of_a_kind1 = win_condition.four_of_a_kind(player1_hand)
    print(four_of_a_kind1)
    four_of_a_kind2 = win_condition.four_of_a_kind(player2_hand)
    print(four_of_a_kind2)
    straight1 = win_condition.straight(player1_hand)
    print(straight1)
    straight2 = win_condition.straight(player2_hand)
    print(straight2)


def main():
    pass


if __name__ == "__main__":
    test()
