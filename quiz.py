import questionary

score = 0

question_bank = [
    {
        "question": "Who was the first Women Prime Minister of Pakistan?",
        "options": ["Benazir Bhutto", "Sheikh Hasina Wazzed", "Hina Rabbina Khar", "None of These"],
        "answer": "Benazir Bhutto",
        "explanation": "Benazir Bhutto is the First Woman Prime Minister of Pakistan"
    },
    {
        "question": "Who is known as the Mother of the Nation of Pakistan?",
        "options": ["Benazir Bhutto", "Faitma Jinnah", "Faitma Sughra", "None of These"],
        "answer": "Faitma Jinnah",
        "explanation": "Faitma Jinnah is the mother of the nation of Pakistan"
    },
    {
        "question": "The national sport of Pakistan is?",
        "options": ["Cricket", "Hockey", "Squash", "Football"],
        "answer": "Hockey",
        "explanation": "Hockey is the national sports game of Pakistan"
    },
    {
        "question": "Which animal is the national animal of Pakistan?",
        "options": ["Tiger", "Lion", "Markhor", "Panda"],
        "answer": "Markhor",
        "explanation": "Markhor is the national animal of Pakistan"
    },
    {
        "question": "Which tree is the national tree of Pakistan?",
        "options": ["Neem", "Sheeshum", "Diyodar", "Date Palm"],
        "answer": "Diyodar",
        "explanation": "Diyodar is the national tree of Pakistan"
    },
    {
        "question": "Which bird is the national bird of Pakistan?",
        "options": ["Cikor", "Eagle", "Pigeon", "Parrot"],
        "answer": "Cikor",
        "explanation": "Cikor is the national bird of Pakistan"
    }
]

for q in question_bank:
    ans = questionary.select(
        q["question"],
        choices=q["options"]
    ).ask()

    if ans == q["answer"]:
        score += 1
        print(f"✅ Correct! {q['explanation']}")
    else:
        print("❌ Wrong Answer")
    print(f"Current Score: {score}\n")

print(f"🎉 Your Final Score is: {score}/{6}")
