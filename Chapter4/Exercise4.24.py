# Game: pick a card 

import random

# Randomly generate a rank between 1 and 13
rank = random.randint(1, 13)

# Randomly generate a suit between 1 and 4
suit = random.randint(1, 4)

# Determine the rank
if rank == 1:
    rank_str = "Ace"
elif rank == 11:
    rank_str = "Jack"
elif rank == 12:
    rank_str = "Queen"
elif rank == 13:
    rank_str = "King"
else:
    rank_str = str(rank)

# Determine the suit
if suit == 1:
    suit_str = "Clubs"
elif suit == 2:
    suit_str = "Diamonds"
elif suit == 3:
    suit_str = "Hearts"
else:
    suit_str = "Spades"

# Display the randomly picked card
print(f'You picked the {rank_str} of {suit_str}.')
