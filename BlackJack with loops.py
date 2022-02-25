# BlackJack
# Author: Lucas Angelozzi
# Date: October 7th, 2021

'''This is the game of blackjack where you can have unlimited cards. you verse the dealer/computer'''

#imports
from random import shuffle
import cards
import random

#Function that creates an ordered deck and then shuffles it. Creates our deck that we will use
def shuffle_deck():
    """This function creates an ordered deck from the cards library that I imported and then shuffles the deck. 
    It will then return the shuffled deck as a list

    Returns:
        List: a list with all of the cards in a deck that are shuffled/in random order
    """

    deck = cards.make_deck()
    cards.shuffle_deck(deck)

    return deck

#global variables
game_deck = shuffle_deck()
player_hand = []
dealer_hand = []
player_value = []
dealer_value = []
player_wins = 0
player_losses = 0


#function to add a card to the end of the hand lists and returns the card value 
def add_card(hand):
    """This function appends a card to the end of a list and then returns the value of that card as an integer

    Args:
        hand (List): a list that you want to append a card to the end of

    Returns:
        Int: the value of the card that has just been added to the list
    """

    card = cards.deal_card(game_deck)
    hand.append(card)

    return cards.card_values[card.value]

#creating the first 2 cards in each hand and adding their value to a respective total
def deal_first_cards():
    """This function adds 2 cards to both dealer and player hands as well as adds their value to the value list
    """

    player_value.append(add_card(player_hand))
    player_value.append(add_card(player_hand))
    dealer_value.append(add_card(dealer_hand))
    dealer_value.append(add_card(dealer_hand))

#funtion to show the beginning stats of the game
def show_beginning_stats():
    """This function prints out the players first two cards as list items, and shows only one of the dealer cards as a list item
    """
    
    print(f"Player card 1: {player_hand[0]}")
    print(f"Player card 2: {player_hand[1]}\n")
    print(f"Dealer card 1: Hidden")
    print(f"Dealer card 2: {dealer_hand[1]}")


#function to decide whether ace is 11 or 1 
def ace_value(hand):
    """This function looks for an 11 in the player value list and then changes it to a 1 if there is momre that 21 total points

    Args:
        hand (list): the value list that contains the 11
    """
    if sum(hand) > 21:
        if 11 in hand:
            hand.remove(11)
            hand.append(1)
        else:
            pass


#function to ask player for another card
def ask_player_for_card():
    """This function asks the player whether or not they would like another card and collects their input as a string variable "player_choice". 
    If the player says yes, it appends a card to the end of the player hand list and adds the card value to the total player value.
    If the player says no, it passes the function.
    """
    
    global player_value

    while sum(player_value) < 21:
        player_choice = input("Would you like another card (yes/no): ")

        if player_choice.lower() == "no" or player_choice.lower() == "n":
            break

        elif player_choice.lower() == "yes" or player_choice.lower() == "y": 
            player_value.append(add_card(player_hand)) 
            print(f"Player card 3: {player_hand[2]}")

        ace_value(player_value)

#function to decide if the dealer will take another card
def ask_dealer_for_card():
    """This function decided whether the dealer gets another card. 
    If the dealers total value is less than the players then another card is appended to the dealers hand and the value is added to its total.
    """

    global dealer_value
    global player_value
    dealer_card_num = 2

    while sum(dealer_value) < sum(player_value):
        if sum(dealer_value) > sum(player_value):
            print("The dealer holds.")

        elif sum(dealer_value) <= sum(player_value):
            dealer_value.append(add_card(dealer_hand))

        ace_value(dealer_value)
    
    for card in dealer_hand[2:]:
        print(f"The dealer takes another card. Dealer card {dealer_card_num}: {card}")
        dealer_card_num += 1

#decide winner function
def winner():
    """This function evaluates the players total value of their hand and the dealers to decide who wins based on 21 card game rules
    """
    global player_wins
    global player_losses

    if sum(dealer_value) <= 21 and sum(player_value) > 21:
        print("Dealer wins :(")
        player_losses += 1

    elif sum(player_value) <= 21 and sum(dealer_value) <= 21:
        if sum(player_value) > sum(dealer_value):
            print("You win :)")
            player_wins +=1
        elif sum(dealer_value) > sum(player_value):
            print("Dealer wins :(")
            player_losses += 1
        elif (sum(player_value) == sum(dealer_value)):
            print("Tie!")
    
    elif sum(player_value) <= 21 and sum(dealer_value) > 21:
        print("You win :)")
        player_wins +=1

    elif (sum(player_value) > 21 and sum(dealer_value) > 21):
        print("Tie!")

#function to print the final stats of the game 
def show_final_stats():
    """This function simply prints the player and dealers final hands and values
    """

    print(f"Player score: {sum(player_value)}")
    print(f"Player hand: {player_hand}")
    print(f"Dealer score: {sum(dealer_value)}")
    print(f"Dealer hand: {dealer_hand}")

def ask_for_play_again():
    """This function asks the player if they want to play again. If yes then it runs the main function again,
    if no, it prints total wins and losses and then exits.
    """
    
    user_choice = input("\nWould you like to play again? ")
    answer = user_choice.lower()

    while True:
        if answer == "yes" or answer == "y":
            print("\n<--------- New Game --------->")
            main()
        elif answer == "no" or answer == "n":
            print(f"Wins: {player_wins}\nLosses: {player_losses}")
            exit()
        else:
            user_choice = input("\nWould you like to play again? ")
            answer = user_choice.lower()

def clear_hands():
    """This function sets all starting variables back to empty in order to restart the game.
    """
    
    global player_hand
    global dealer_hand
    global player_value
    global dealer_value

    player_hand = []
    dealer_hand = []
    player_value = []
    dealer_value = []

def main():
    clear_hands()
    shuffle_deck()
    deal_first_cards()
    show_beginning_stats()
    print()
    ask_player_for_card()
    print()
    ask_dealer_for_card()
    print()
    winner()
    print()
    show_final_stats()
    ask_for_play_again()
    

if __name__ == "__main__":
    main()