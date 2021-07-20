import random

# Global Variables
i = random.randint(0, 2)
rock_paper_scissors = ["rock", "paper", "scissors"]
computer_choice = rock_paper_scissors[i]
player_choice = input("rock, paper, scissors? ")

# Initalizing Game
print("ROCK, PAPER, SCISSORS...SHOOT!")
if player_choice == "rock" and computer_choice == "scissors":
    print(f"Player's choice: {player_choice} vs Computer's choice: {computer_choice}")
    print("Player wins!")
elif player_choice == "rock" and computer_choice == "paper":
    print(f"Player's choice: {player_choice} vs Computer's choice: {computer_choice}")
    print("Computer wins!")
elif player_choice == "paper" and computer_choice == "rock":
    print(f"Player's choice: {player_choice} vs Computer's choice: {computer_choice}")
    print("Player wins!")
elif player_choice == "paper" and computer_choice == "scissors":
    print(f"Player's choice: {player_choice} vs Computer's choice: {computer_choice}")
    print("Computer wins!")
elif player_choice == "scissors" and computer_choice == "paper":
    print(f"Player's choice: {player_choice} vs Computer's choice: {computer_choice}")
    print("Player wins!")
elif player_choice == "scissors" and computer_choice == "rock":
    print(f"Player's choice: {player_choice} vs Computer's choice: {computer_choice}")
    print("Computer wins!")
elif player_choice == computer_choice:
    print(f"Player's choice: {player_choice} vs Computer's choice: {computer_choice}")
    print("It's a Draw!")