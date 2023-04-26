def calculate_score(questions):   
    import random
    from colored import fg

    random.shuffle(questions)
    num_correct = 0
    for i, question in enumerate(questions):
        
        print(fg('white') + f"Question {i+1}: {question['question']}")
        options = [question['option1'], question['option2'], question['option3'], question['option4']]
        random.shuffle(options)
        for j, option in enumerate(options):
            print(f"   ({j+1}) {option}")
        
        while True:
            user_answer = input("Your answer: ")
            if user_answer.isdigit() and 1 <= int(user_answer) <= len(options):
                user_answer = int(user_answer)
                break
            else:
                print("Invalid input. Please enter the number of the correct answer.")
        
        if options[user_answer - 1] == question['answer']:
            
            print(fg('blue') + "Correct!\n")
            num_correct += 1
        else:
            color = fg('red')
            print(color + f"Incorrect. The correct answer is: {question['answer']}\n")
    
    score = num_correct / len(questions) * 100
    score = round(score, 2)
    return score

def calculate_winner(teams : list) -> list:
    scores = []
    for team in teams:
        for score in team.keys():
            team_score = {'team_name': score, 'score': team[score]["score"], 'names': team[score]['names'] }
            scores.append(team_score)
    newlist = sorted(scores, key=lambda score: score['score'], reverse = True) 
    return newlist   
