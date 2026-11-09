# 🧠 QuizMaster – Python Quiz Application

## Introduction

QuizMaster is an interactive Python Quiz Application developed as part of my Week 6 Python Development Internship Capstone Project.

The application allows users to answer multiple-choice questions, calculate scores automatically and review their performance.

## Project Objectives

- Develop a complete Python application.
- Create an interactive quiz interface.
- Implement automatic score calculation.
- Store quiz results using SQLite.
- Apply exception handling and logging.
- Maintain clean and modular code.
- Document the project architecture.

## Technologies Used

- Python
- Streamlit
- SQLite
- JSON
- GitHub

## Features

1. Interactive quiz interface.
2. Multiple-choice questions.
3. Four answer options per question.
4. Automatic score calculation.
5. Percentage-based performance summary.
6. Correct answer review.
7. SQLite database integration.
8. Recent quiz results.
9. Exception handling.
10. Application logging.

## Project Structure

QuizMaster-Python-Capstone/

- app.py
- database.py
- quiz_logic.py
- requirements.txt
- README.md
- .gitignore
- data/
  - questions.json

## Application Architecture

The application is divided into three main Python modules.

### 1. app.py
Handles the user interface, quiz interaction and result display.

### 2. database.py
Handles SQLite database creation, saving quiz results and retrieving previous results.

### 3. quiz_logic.py
Handles question loading, validation and score calculation.

## Database Schema

The application uses SQLite to store quiz results.

| Column | Description |
|---|---|
| id | Unique result ID |
| player_name | Participant name |
| score | Correct answers |
| total_questions | Total questions |
| percentage | Final percentage |
| created_at | Result date and time |

## Installation

Install the required dependency:

pip install -r requirements.txt

## Run Application

Use the following command:

streamlit run app.py

The application will open in your browser.

## Testing

The application can be tested by:

- Entering a participant name.
- Answering all quiz questions.
- Submitting the quiz.
- Checking the final score.
- Reviewing correct answers.
- Checking saved results.

## Exception Handling and Logging

The application includes exception handling to manage errors during question loading and database operations.

Logging is used to record important application events and errors.

## Deployment

The application can be deployed using Streamlit Community Cloud.

Website:
https://share.streamlit.io/

Steps:

1. Upload the project to GitHub.
2. Sign in to Streamlit Community Cloud.
3. Connect the GitHub repository.
4. Select app.py as the main file.
5. Deploy the application.

## Conclusion

QuizMaster demonstrates practical Python application development using Streamlit and SQLite.

This project helped me understand modular programming, database integration, JSON handling, exception handling, logging and interactive application development.

**Internship Module:** Week 6 – Python Capstone Project.
