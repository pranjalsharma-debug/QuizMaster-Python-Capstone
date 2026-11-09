import json
from pathlib import Path


def load_questions(file_path):

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError("Questions file not found.")

    with path.open("r", encoding="utf-8") as file:
        questions = json.load(file)

    if not isinstance(questions, list) or not questions:
        raise ValueError("Invalid questions data.")

    required = {
        "question",
        "options",
        "answer",
        "explanation"
    }

    for question in questions:

        if not required.issubset(question):
            raise ValueError("Invalid question structure.")

        if len(question["options"]) != 4:
            raise ValueError("Each question needs four options.")

        if question["answer"] not in question["options"]:
            raise ValueError("Correct answer is missing from options.")

    return questions


def calculate_score(questions, selected_answers):

    score = 0
    feedback = []

    for index, question in enumerate(questions):

        selected = selected_answers.get(index)

        correct = selected == question["answer"]

        if correct:
            score += 1

        feedback.append({
            "number": index + 1,
            "question": question["question"],
            "selected": selected or "Not answered",
            "correct_answer": question["answer"],
            "correct": correct,
            "explanation": question["explanation"]
        })

    return score, feedback
