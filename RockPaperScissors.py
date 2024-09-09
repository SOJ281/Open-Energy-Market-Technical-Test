import random
import networkx as nx

#RockPaperScissors

#Regular rock paper Scissors
def rockPaperScissors():
    choices = ["rock", "paper", "scissors"]
    #directed graph of Win/Lose/Draw Conditions
    #e.g. rock -> scissors
    winStrats = nx.DiGraph()
    winStrats.add_edges_from([("rock", "scissors"),
                          ("paper", "rock"), ("scissors", "paper")])

    
    playerChoice = input("Select a rock/paper/scissors:")

    while playerChoice not in choices:
        playerChoice = input("Select a VALID rock/paper/scissors:")
        
    compChoice = choices[random.randrange(0,3)]

    print(playerChoice + " VS. " + compChoice)

    if playerChoice == compChoice:
        print("Draw")
    elif(playerChoice, compChoice) in winStrats.out_edges(playerChoice):
        print("WIN!")
    else:
        print("LOSE!")

#Irregular
def rockPaperScissorsLizardSpock():
    choices = ["rock", "paper", "scissors", "lizard", "Spock"]
    #directed graph of Win/Lose/Draw Conditions
    #e.g. rock -> scissors
    winStrats = nx.DiGraph()
    winStrats.add_edges_from([("rock", "scissors"), ("rock", "lizard"),
                              ("paper", "rock"), ("paper", "Spock"),
                              ("scissors", "paper"), ("scissors", "lizard"),
                              ("Spock", "scissors"), ("Spock", "rock"),
                              ("lizard", "Spock"), ("lizard", "paper")])

    
    playerChoice = choices[random.randrange(0,5)]
    while True:
        comp2Choice = playerChoice
        playerChoice = input("Select a rock/paper/scissors/lizard/Spock/kill:")
        if playerChoice == "kill": break

        while playerChoice not in choices:
            playerChoice = input("Select a VALID rock/paper/scissors/lizard/Spock/kill:")
            if playerChoice == "kill": break
            
        comp1Choice = choices[random.randrange(0,5)]

        print("Computer 1:" + comp1Choice)
        print("Computer 2:" + comp2Choice)

        print("player VS. computer 1")
        if playerChoice == comp1Choice:
            print("Draw")
        elif(playerChoice, comp1Choice) in winStrats.out_edges(playerChoice):
            print("WIN!")
        else:
            print("LOSE!")
            

        print("player VS. computer 2")
        if playerChoice == comp2Choice:
            print("Draw")
        elif(playerChoice, comp2Choice) in winStrats.out_edges(playerChoice):
            print("WIN!")
        else:
            print("LOSE!")


choice = input("Regular rock(1) or with spock(2)")
if choice == "1":
    rockPaperScissors()
elif choice == "2":
    rockPaperScissorsLizardSpock()
else:
    print("Wrong choice")
