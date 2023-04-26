def generate_questions():
    import csv
    with open('questions.csv', newline='') as file:
        reader = csv.DictReader(file)
        questions = [row for row in reader]
    return questions