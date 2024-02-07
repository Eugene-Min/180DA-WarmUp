import random
player_choice = ""
while(player_choice != 'q'):
    player_choice = input('Please choose rock (r), paper (p), or scissors (s) or to quit (q).\n')
    computer_choice = random.randint(0,2)
    if(player_choice == 'r'):
        if(computer_choice == 0): #rock
            print("You chose rock.\n")
            print("The computer chose rock.\n")
            print("You tied.\n")
        elif(computer_choice == 1): #paper
            print("You chose rock.\n")
            print("The computer chose paper.\n")
            print("You lost.\n")
        elif(computer_choice == 2): #scissors
            print("You chose rock.\n")
            print("The computer chose scissors.\n")
            print("You win!\n")
    elif(player_choice == 'p'):
        if(computer_choice == 0): #rock
            print("You chose paper.\n")
            print("The computer chose rock.\n")
            print("You win!\n")
        elif(computer_choice == 1): #paper
            print("You chose paper.\n")
            print("The computer chose paper.\n")
            print("You tied.\n")
        elif(computer_choice == 2): #scissors
            print("You chose paper.\n")
            print("The computer chose scissors.\n")
            print("You lost.\n")
    elif(player_choice == 's'):
        if(computer_choice == 0): #rock
            print("You chose scissors.\n")
            print("The computer chose rock.\n")
            print("You lost.\n")
        elif(computer_choice == 1): #paper
            print("You chose scissors.\n")
            print("The computer chose paper.\n")
            print("You win!\n")
        elif(computer_choice == 2): #scissors
            print("You chose scissors.\n")
            print("The computer chose scissors.\n")
            print("You tied.\n")
    else: 
        print("Invalid input")
    

