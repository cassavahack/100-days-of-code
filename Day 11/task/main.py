# import art
# import random
# # list of cards with 11 being an ace
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#
# # player_choice= input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
# # if player_choice == "n":
#
# #function that randomly chooses a card
# def deal_card(cards):
#     return random.choice(cards)
#
#
# #Empty list for user and computer to store cards in
# user_cards = []
# computer_cards = []
#
#
#
# #deal two random cards to user
# for _ in range(2):
#     user_cards.append(deal_card(cards))
#
#
# #deal two random cards to computer
# for _ in range(2):
#     computer_cards.append(deal_card(cards))
# print(computer_cards)
#
# #function that adds up list of cards as input.
# def calculate_score(hand):
#     if sum(hand) == 21 and len(hand) == 2:
#         return 0  # special value for blackjack
#
#     if 11 in hand and sum(hand) > 21:
#         hand.remove(11)
#         hand.append(1)
#
#     return sum(hand)
#
# # Checks user hand and computer hand and ends game if winning criteria is met
# while True:
#     final_user_score = calculate_score(user_cards)
#     computer_score = calculate_score(computer_cards)
#     if final_user_score > 21:
#         print(f"Your score was {final_user_score} and hand was {user_cards} computers score was {computer_score} you lose")
#         break
#     elif final_user_score == 0 and computer_score!= 0:
#         print(f"You win your final score was {final_user_score} and hand was {user_cards} and computer score was {computer_score}")
#         break
#     elif computer_score == 0:
#         print(f"Your score was {final_user_score} and hand was {user_cards}computers score was {computer_score} you lose")
#         break
#
#     print(f"Your cards: {user_cards}, current score: {final_user_score}")
#     print(f"Computer's first card: {computer_cards[0]}")
#
#     choice = input("Type 'y' to draw another card, 'n' to pass: ").strip().lower()
#     if choice == 'y':
#         user_cards.append(deal_card(cards))
#     elif choice == 'n':
#         break
#     else:
#         print("Please type 'y' or 'n'.")




import art
import random

# list of cards with 11 being an ace
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# function that randomly chooses a card
def deal_card(cards):
    return random.choice(cards)

# Empty list for user and computer to store cards in
user_cards = []
computer_cards = []

# deal two random cards to user
for _ in range(2):
    user_cards.append(deal_card(cards))

# deal two random cards to computer
for _ in range(2):
    computer_cards.append(deal_card(cards))

print(computer_cards)

# function that adds up list of cards as input.
def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0  # special value for blackjack

    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)

    return sum(hand)

# NEW: compare() per your spec
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw."
    elif computer_score == 0:
        return "Computer has blackjack. You lose."
    elif user_score == 0:
        return "Blackjack! You win."
    elif user_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Computer went over. You win."
    elif user_score > computer_score:
        return "You win."
    else:
        return "You lose."

# Checks user hand and computer hand and ends game if winning criteria is met
while True:
    final_user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    if final_user_score > 21:
        print(f"Your score was {final_user_score} and hand was {user_cards}. Computer's score was {computer_score}. You lose.")
        break
    elif final_user_score == 0 and computer_score != 0:
        print(f"You win! Your final score was {final_user_score} and hand was {user_cards}. Computer score was {computer_score}.")
        break
    elif computer_score == 0:
        print(f"Your score was {final_user_score} and hand was {user_cards}. Computer's score was {computer_score}. You lose.")
        break

    print(f"Your cards: {user_cards}, current score: {final_user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    choice = input("Type 'y' to draw another card, 'n' to pass: ").strip().lower()
    if choice == 'y':
        user_cards.append(deal_card(cards))
    elif choice == 'n':
        break
    else:
        print("Please type 'y' or 'n'.")

# Dealer phase and final outcome after player stands or early end
final_user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

# Dealer draws if game not already decided by blackjack or player bust
if final_user_score != 0 and final_user_score <= 21 and computer_score != 0:
    while computer_score < 17:
        computer_cards.append(deal_card(cards))
        computer_score = calculate_score(computer_cards)

# Show final hands and scores
print(f"Your final hand: {user_cards}, final score: {final_user_score}")
print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

# Decide winner using compare()
print(compare(final_user_score, computer_score))