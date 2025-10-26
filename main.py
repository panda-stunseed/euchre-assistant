# Import the abstact card class
from pygame_cards.abstract import AbstractCard

from dataclasses import dataclass


@dataclass
class Card(AbstractCard):
    """A card from a standard card deck 

    """

    number: int
    suit: int
    face: str = ""  



if __name__ == "__main__":
    card = Card(
        name = "10 diamonds",
        number = 10,
        suit = "Diamond" 
    )

    print(card)

# Deal to players (4)
# Define Trump Card 
# Play the game 
#   a. First card plays (dealer first?)
#   b. Player turn clockwise
#   c. Enforce rules on each turn 
#   d. 5 times 
# Count score (however that's done) 
# Player with highest score wins 
