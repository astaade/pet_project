# player.py

class Player:
    """Player class tracks player state across game session"""
    
    def __init__(self, name):
        """Initialize player attributes"""
        self.name = name
        self.num_guesses = 0
        
    def increment_guesses(self):
        """Increase number of guesses by player by 1"""
        self.num_guesses += 1
        
    def reset(self):
        """Reset player state for new game"""
        self.num_guesses = 0

# Usage
player1 = Player("John")
print(f"Number of guesses: {player1.num_guesses}")

player1.increment_guesses()
print(f"Number of guesses after increment: {player1.num_guesses}") 

player1.reset()
print(f"Reset number of guesses: {player1.num_guesses}")