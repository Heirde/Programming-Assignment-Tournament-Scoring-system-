teams = []
individuals = []
scores_team = []
scores_individual = []
 
#This section is where I built the functions for my team part of the tournament.
def team_score_system():
        for i in range(4):
            score_add = int(input("What was the score?:> "))
            seperator()
            scores_team.append(score_add)
 
#Here I created the leaderboard where I made use of things like Lambda which was recommended by Micheal which creates a nameless function.
def team_leaderboard():
    team_data = list(zip(teams, scores_team))
    team_data.sort(key = lambda x: x[1], reverse = True)
 
    seperator()
     #Here I made use of the enumerate function which creats a counter that starts at 1 which can be used for the variable rank. This then lists each team with their score and their rank
    for rank, (team, score) in enumerate(team_data, 1):
        if rank == 1:
              print(f"1st Place: {team} - {score} points")
        elif rank == 2:
              print(f"2nd Place: {team} - {score} points")
        elif rank == 3:
              print(f"3rd Place: {team} - {score} points")
        else:
             print(f"{rank}th Place: {team} - {score} points")
 
     
     
################################################################################
       
#This section is where I built the function for my individual part of the tournament.
def individual_score_system():
     for i in range(20):
          score_add = int(input("What was the score?:> "))
          seperator()
          scores_individual.append(score_add)
 
#Here I created the leaderboard where I made use of things like Lambda which was recommended by Micheal.
def individual_leaderboard():
    #Here there is the list and zip function. Zip just brings two lists together and then the list function turns it back into the list data type.
    individual_data = list(zip(individuals, scores_individual))
    #This part then puts this list in order and then uses the lambda to create a nameless function. x is what it grabs from the list and it then grabs the x[1] index next to that item.
    individual_data.sort(key = lambda x: x[1], reverse = True)
   
    #Here I made use of the enumerate function which creats a counter that starts at 1 which can be used for the variable rank. This then lists each individual with their score and their rank
    for rank, (individual, score) in enumerate(individual_data, 1):
        print("=== These are the Final results for:", event_type, "=== ")
        if rank == 1:
              print(f"1st Place: {individual} - {score} points")
        elif rank == 2:
              print(f"2nd Place: {individual} - {score} points")
        elif rank == 3:
              print(f"3rd Place: {individual} - {score} points")
        else:
             print(f"{rank}th Place: {individual} - {score} points")
 
        seperator()
 
#############################################################
#Here I created a quick function that creates a seperator that i can call where I want it which makes it easier to write.
def seperator():
    print("=" * 20)
#############################################################
seperator()
print("=== WELCOME TO THE TOURNAMENT SCOREBOARD! ===")
seperator()
 
team_type = input("Is this a team or individual event?:>")
 
seperator()
 
#Here is the team section. I decided here I would also put all the functions at the start where I would call them in the if statement as i did in individuals.
if team_type == "team":
    for i in range(4):
        add_teams = input("What are your team names?:> ")
        seperator()
        teams.append(add_teams)
    event_type = input("What type of event is this?(Esports, Sports, Educational (Maths, Science etc),Coding:> ")
    if event_type not in ["Esports", "Sports", "Educational", "Coding"]:
        seperator()
        print("Incorrect input. Please enter one of the following: Esports, Sports, Educational, Coding.")
    else:
        team_score_system()
        team_leaderboard()
    seperator()
 
 
#Here is the individual section. I decided since I put all of the functions at the start I would call them in the if statement.
elif team_type == "individual":
    for i in range(20):
        add_individuals = input("What is the name of your individual?> ")
        seperator()
        individuals.append(add_individuals)
    event_type = input("What type of event is this?(Esports, Sports, Educational (Maths, Science etc),Coding:> ")
    if event_type not in ["Esports", "Sports", "Educational", "Coding"]:
        seperator()
        print("Incorrect input. Please enter one of the following: Esports, Sports, Educational, Coding.")
    else:
        individual_score_system()
        individual_leaderboard()
    seperator()
 
#I created this as part of my else if the user ever inputs something incorrect it is in place to help them
else:
    seperator()
    print("incorrect input. (Can only be either team or individual!")
    seperator()