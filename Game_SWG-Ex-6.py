import random
def SWG_game():
    user_winner = 0
    comp_winner = 0
    l = ["snack", "water", "gun"]
    i = 10
    while (i):
        comp_choice = random.randint(1, 3)
        print("1. snack\n")
        print("2. water\n")
        print("3. gun\n")
        user_choice = int(input("Enter your choice : \n"))

        if comp_choice == user_choice:
            print(f"\n computer choose  {l[comp_choice - 1]} ,so both you give 0 point ")
        elif comp_choice == 1:
            if user_choice == 2:
                print(f"\ncomputer choose {l[comp_choice - 1]},So you lost the game")
                comp_winner += 1
            else:
                print(f"\ncomputer choose {l[comp_choice - 1]},So you win the game")
                user_winner += 1
        elif comp_choice == 2:
            if user_choice == 3:
                print(f"\ncomputer choose {l[comp_choice - 1]},So you lost the game")
                comp_winner += 1
            else:
                print(f"\ncomputer choose {l[comp_choice - 1]},So you win the game")
                user_winner += 1
        else:
            if user_choice == 1:
                print(f"\ncomputer choose {l[comp_choice - 1]},So you lost the game")
                comp_winner += 1
            else:
                print(f"\ncomputer choose {l[comp_choice - 1]},So you win the game")
                user_winner += 1

        i -= 1

    if user_winner > comp_winner:
        print(f"\nYou win {user_winner} game and computer win {comp_winner} game")
        print("\n congratulations you WIN the game")
    elif user_winner < comp_winner:
        print(f"\nYou win {user_winner} game and computer win {comp_winner} game")
        print("\nyou lost the game")
        print("TRU AGAIN!")
    else:
        print(f"\nYou win {user_winner} game and computer win {comp_winner} game")
        print("\nNone of you winner !")

SWG_game()