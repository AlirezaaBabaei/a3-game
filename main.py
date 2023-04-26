import pygame
from read_file import generate_questions
from locations import location_finder
from calculate_score import calculate_score

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
        team[team_name] = players
        
        location_finder()
        questions = generate_questions()
        score = calculate_score(questions)
        print(f"{team_name}'s score is {score}%")
        
        pygame.init()
        pygame.mixer.music.load("end.mp3")
        pygame.mixer.music.play()
        break

if __name__ == "__main__":
    main()
