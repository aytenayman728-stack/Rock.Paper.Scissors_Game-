p1_score = 0 #123
p2_score = 0 #890
round_number = 1

while round_number != 3 :
    print (f"---- ROUND {round_number} ----")
    battle_code = input(" enter 2-digit battle code : ")

      #Input  validation 
    if len(battle_code) != 2 :
        print ("invalid battle code ")
        continue

      #speed trap
    if battle_code[0] in "123" and battle_code[1] in "890":
        player1 = battle_code[0]
        player2 = battle_code[1]
    elif battle_code[1] in "123" and battle_code [0] in "890":
        player1 = battle_code[1]
        player2 = battle_code[0]
    else :
       print ("invalid battle code ! p1 uses 1,2,3 and p2 uses 8,9,0")
       continue

      #translation engine player 1
    if player1 == "1" :
        player1_choice = "rock"
    elif player1 == "2" :
        player1_choice = "paper"
    else :
        player1_choice = "scissors"

      #translation engine player 2
    if player2 == "8" :
        player2_choice = "rock"
    elif player2 == "9" :
        player2_choice = "paper"
    else :
        player2_choice = "scissors"
    
    print (f"player 1 chose {player1_choice}")
    print (f"player 2 chose {player2_choice}")


        #combat engine 
    if player1_choice == player2_choice :
        print ("It's a tie")
    elif player1_choice == "rock" and player2_choice == "scissors" :
        print ("player 1 win !")
        p1_score +=1 
    elif player1_choice == "scissors" and player2_choice == "paper" :
        print ("player 1 win !")
        p1_score +=1 
    elif player1_choice == "paper" and player2_choice == "rock" :
        print ("player 1 win !")
        p1_score +=1
    else :
        print ("palyer 2 win !")
        p2_score +=1 
 

    round_number += 1