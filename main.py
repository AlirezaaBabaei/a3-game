import pygame
from read_file import generate_questions
from locations import location_finder
from calculate_score import calculate_score, calculate_winner

teams = [{ 'Team1' : {"names": [], "score": 55.0}},
          {'Team2' : {"names": [], "score": 60.0}}]

TEAM_1 = { 'Team1' : {"names": [], "score": 55.0}}
TEAM_2 = { 'Team2' : {"names": [], "score": 60.0}}

def print_ranking(ranking : list):
    print("---- RANKING ----")
    for team in ranking:
        print(f"{team['team_name']}: {team['score']}%")


def main():
    pygame.init()
    pygame.mixer.music.load("intro.mp3")
    pygame.mixer.music.play()
    print("\nWelcome to our Quiz\n")
    while True:
        players_num = input("How many members are in your team? (at least 2): ")
        try:
            players_num = int(players_num)
            if players_num < 2:
                raise ValueError
        except ValueError:
            print("Error: Please enter a number greater than or equal to 2.")
            continue
        
        team = {}
        team_name = input("What's the team name: ")
        players = []
        for i in range(1, players_num + 1):
            name = input(f"What is the name of player {i}: ")
            players.append(name)
        team[team_name] = {}
        team[team_name]["names"] = players
        team[team_name]["score"] = 0
        teams.append(team)
        print(teams)
        
        location_finder()
        questions = generate_questions()
        team[team_name]["score"] = calculate_score(questions)
        print(f"{team_name}'s score is {team[team_name]['score']}%")
        ranking = calculate_winner(teams)
        print_ranking(ranking)
        pygame.init()
        pygame.mixer.music.load("end.mp3")
        pygame.mixer.music.play()
        break

if __name__ == "__main__":
    main()
