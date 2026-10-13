"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""



def value_of_card(card):
    """Determine the scoring value of a card."""
    if card in ("J", "Q", "K"):
        return 10
    if card == "A":
        return 1
    return int(card)

#Second Solutions
    #card_dict = { "J": 10, "Q": 10, "K": 10, "1": 1,"A": "1", "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10 }
        #if card in card_dict:
            #return card_dict[card]
    

def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand."""
    val_one = value_of_card(card_one)
    val_two = value_of_card(card_two)

    if val_one > val_two:
        return card_one
    if val_two > val_one:
        return card_two
    return card_one, card_two



def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card."""

    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)

    if card_one == "A" or card_two == "A":
        return 1 
    elif card_one_value + card_two_value <= 10:
            return 11
    else:
        return 1



def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'."""

    ten_cards = ("10", "J", "Q", "K")
    if (card_one == "A" and card_two in ten_cards) or (card_two == "A" and card_one in ten_cards):
        return True
    else:
        return False
    

def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands."""
    return value_of_card(card_one) == value_of_card(card_two)



    
def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet."""
    total = value_of_card(card_one) + value_of_card(card_two)
    return total in (9, 10, 11)