#Welcome To my Tournament scoreboard system

#Lists for user to add data to
teams = []
individuals = []
scores_team = []
scores_individual = []
team_ranks = []
individual_ranks = []
team_players = []

#Here I built the leaderboard system for both team and individual
def team_leaderboard():
    global teams, scores_team, team_ranks
    team_data = list(zip(teams, scores_team, team_ranks))
    team_data.sort(key = lambda x: x[1], reverse = True)

    for (team, score, rank) in team_data:
        print(f"Team: {team}. Scored: {score} points and their rank is: {rank}")
        seperator()
        
def individual_leaderboard():
    global individuals, scores_individual, individual_ranks
    individual_data = list(zip(individuals, scores_individual, individual_ranks))
    individual_data.sort(key = lambda x: x[1], reverse = True)
  
    for (individual, score, rank) in individual_data:
        print(f"Team: {individual}. Scored: {score} points and their rank is {rank}")
        seperator()

#Here I built the score systems for both team and individual        
def team_score_system():
        global teams, scores_team, team_ranks
        print("Teams:", teams)
        seperator()
        for i in range(4):
            print("What was the score for team", i + 1,"Score between 1 - 20")
            score_add = int(input(":> "))
            if score_add <=5:
                rank_team = "Rank 4"
            elif score_add <=10:
                rank_team = "Rank 3"
            elif score_add <=15:
                rank_team = "Rank 2"
            else:
                rank_team = "Rank 1"
            team_ranks.append(rank_team)
            seperator()
            scores_team.append(score_add)
        team_leaderboard()   

def individual_score_system():
    global individuals, scores_individual, individual_ranks
    print("Individuals:", individuals)
    seperator()
    for i in range(20):
        print("What was individual", i + 1, "score (Score between 1 - 20)")
        score_add = int(input(":> "))
        if score_add <=5:
            rank_individual = "Rank 4"
        elif score_add <=10:
            rank_individual = "Rank 3"
        elif score_add <=15:
            rank_individual = "Rank 2"
        else:
            rank_individual = "Rank 1"
        individual_ranks.append(rank_individual)
        seperator()
        scores_individual.append(score_add)
    individual_leaderboard()

#Seperator line function with lambda
seperator = lambda: print("=" * 60)

#Welcome message
seperator()
print("=== WELCOME TO THE TOURNAMENT SCOREBOARD! ===")
seperator()

#Picking whether it is team or individual event
team_type = int(input("Is this a 1.team or 2.individual event? (input 1 for Teams or 2 for Individuals):>"))

seperator()

#Team Section
if team_type == 1: 
    for i in range(4):
        add_teams = input("What are your team names?(Enter one team at a time and press enter!!):> ")
        seperator()
        teams.append(add_teams)
        for i in range(5):
            i += 1
            add_players = input("What is the name of your player?(Will repeat 5 times add one player at a time!!!):> ")
            seperator()
            team_players.append(add_players)
    
    while True:
        event_type = input("What is the event?(Esports, Sports, Educational (Maths, Science etc),Coding(Has to be spelled exactly!!!):> ").lower()
        if event_type in ["esports", "sports", "educational", "coding"]:
            break
        elif event_type not in ["esports", "sports", "educational", "coding"]:
            for i in range(4):
                i += 1
                print("attempt", i)
                print("Incorrect input. Please enter one of the following: esports", "sports", "educational", "coding")

                if i == 3:
                    print("Exiting the program due to many failed attempts")
                    exit()
                    
                print("Please Try again") 
            
                event_type = input("What is the event?(Esports, Sports, Educational (Maths, Science etc),Coding(Has to be spelled exactly!!!):> ").lower()
                if event_type in ["esports", "sports", "educational", "coding"]:
                    break   
            break
        
    team_score_system()           

#Individual Section
elif team_type == 2:
    for i in range(20):
        add_individuals = input("What is the name of your individual?(Will repeat 20 times, add one person at a time!!)> ")
        seperator()
        individuals.append(add_individuals)
    while True:
        event_type = input("What is the event?(Esports, Sports, Educational (Maths, Science etc),Coding(Has to be spelled exactly!!!):> ").lower()
        if event_type in ["esports", "sports", "educational", "coding"]:
            if event_type == "esports":
                print()
            break
        elif event_type not in ["esports", "sports", "educational", "coding"]:
            for i in range(4):
                i += 1
                print("attempt", i)
                print("Incorrect input. Please enter one of the following: esports", "sports", "educational", "coding")

                if i == 3:
                    print("Exiting the program due to many failed attempts")
                    exit()
                    
                print("Please Try again")   
                
                event_type = input("What is the event?(Esports, Sports, Educational (Maths, Science etc),Coding(Has to be spelled exactly!!!):> ").lower()
                if event_type in ["esports", "sports", "educational", "coding"]:
                    break   
            break
        
    individual_score_system() 

#Extra ElSE incase user inputs incorrect number
else:
    seperator()
    print("incorrect input. (Can only be either 1.team or 2.individual!")
    seperator()