questions = [
    {
        "prompt": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "prompt": "Which language is primarily spoken in Brazil?",
        "options": ["A. Spanish", "B. Portuguese", "C. English", "D. French"],
        "answer": "B"
    },
    {
        "prompt": "What is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
        "answer": "B"
    },
    {
        "prompt": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"],
        "answer": "A"
    },
    {
        "prompt": "What is the chemical symbol for water?",
        "options": ["A. H2O", "B. O2", "C. CO2", "D. HO"],
        "answer": "A"
    },
    {
        "prompt": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "prompt": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "answer": "D"
    },
    {
        "prompt": "Who painted the Mona Lisa?",
        "options": ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Claude Monet"],
        "answer": "C"
    },
    {
        "prompt": "What is the hardest natural substance on Earth?",
        "options": ["A. Gold", "B. Iron", "C. Diamond", "D. Silver"],
        "answer": "C"
    },
    {
        "prompt": "In which year did the Titanic sink?",
        "options": ["A. 1905", "B. 1912", "C. 1918", "D. 1925"],
        "answer": "B"
    },
    {
        "prompt": "Which element has the atomic number 1?",
        "options": ["A. Helium", "B. Hydrogen", "C. Oxygen", "D. Carbon"],
        "answer": "B"
    },
    {
        "prompt": "Which continent is the Sahara Desert located in?",
        "options": ["A. Asia", "B. North America", "C. Africa", "D. Australia"],
        "answer": "C"
    },
    {
        "prompt": "Who developed the theory of relativity?",
        "options": ["A. Isaac Newton", "B. Albert Einstein", "C. Galileo Galilei", "D. Nikola Tesla"],
        "answer": "B"
    },
    {
        "prompt": "What is the largest mammal in the world?",
        "options": ["A. Elephant", "B. Blue Whale", "C. Great White Shark", "D. Giraffe"],
        "answer": "B"
    },
    {
        "prompt": "Which country is known as the Land of the Rising Sun?",
        "options": ["A. China", "B. South Korea", "C. Japan", "D. Thailand"],
        "answer": "C"
    },
    {
        "prompt": "What is the chemical symbol for gold?",
        "options": ["A. Au", "B. Ag", "C. Fe", "D. Pb"],
        "answer": "A"
    },
    {
        "prompt": "Which organ in the human body is responsible for pumping blood?",
        "options": ["A. Brain", "B. Lungs", "C. Heart", "D. Liver"],
        "answer": "C"
    },
    {
        "prompt": "Which gas is most abundant in the Earth's atmosphere?",
        "options": ["A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Hydrogen"],
        "answer": "C"
    },
    {
        "prompt": "Who invented the telephone?",
        "options": ["A. Thomas Edison", "B. Alexander Graham Bell", "C. Nikola Tesla", "D. Guglielmo Marconi"],
        "answer": "B"
    },
    {
        "prompt": "Which country hosted the 2016 Summer Olympics?",
        "options": ["A. China", "B. United States", "C. Brazil", "D. Japan"],
        "answer": "C"
    },
    {
        "prompt": "What is the square root of 64?",
        "options": ["A. 6", "B. 7", "C. 8", "D. 9"],
        "answer": "C"
    }
]



Score=0
for question in questions:
    print(question["prompt"])
    for option in question["options"]:
        print(option)
    answer=input("Enter your answer(A,B,C,D): ").upper()
    if answer==question["answer"]:
        print("Correct, hooray!! \n")
        Score+=1
    else:
        print(f"Wrong, Looser!!!. The correct answer is {question["answer"]}")

print(f"You got {Score} out of {len(questions)} questions")