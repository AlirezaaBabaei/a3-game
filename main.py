# First welcome message Quiz
# How many players (at least 2)
# On an other computer you would like to have also another group
# Asking for the teams names
# Asking about the names of the players and add them into the team.
# all of the players are in one team
# Ask each group about 10 quations
# Calculate how many quations are correct
# Hardcode 2 groups with names and calculate the score
# Printing the winner

from read_file import generate_questions
from locations import location_finder
from calculate_score import calculate_score

def main():
    print("Welcome to our Quiz")
    while True:
        players_num = input("How many members are in your team? (at least 2): ")
        try:
            players_num = int(players_num)
        except:
            continue
        if players_num >= 2:
            team = {}
            team_name = input("What's the team name: ")
            players = []
            for i in range(1, players_num + 1):
                name = input(f"What is the name of player {i}: ")
                players.append(name)
            team[team_name] = players
        location_finder()
        questions = generate_questions()
        score = calculate_score(questions)
        print(f"{team_name}'s score is {score}%")
        break

if __name__ == "__main__":
    main()
