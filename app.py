import streamlit as st
import logging
from database import initialize_database, save_result, get_recent_results
from quiz_logic import load_questions, calculate_score

logging.basicConfig(
    filename="quizmaster.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

st.set_page_config(
    page_title="QuizMaster",
    page_icon="🧠",
    layout="centered"
)

initialize_database()

st.title("🧠 QuizMaster")
st.subheader("Test Your Knowledge!")
st.write("Answer the questions and check your score.")

try:
    questions = load_questions("data/questions.json")
except Exception as error:
    logger.exception("Question loading failed")
    st.error(f"Unable to load questions: {error}")
    st.stop()

if "submitted" not in st.session_state:
    st.session_state.submitted = False

if "saved" not in st.session_state:
    st.session_state.saved = False

if not st.session_state.submitted:

    with st.form("quiz_form"):

        name = st.text_input("Enter Your Name")

        answers = {}

        for i, question in enumerate(questions):
            st.write(f"### Question {i + 1}")
            st.write(question["question"])

            answers[i] = st.radio(
                "Select your answer:",
                question["options"],
                index=None,
                key=f"question_{i}"
            )

        submit = st.form_submit_button("Submit Quiz")

    if submit:

        if not name.strip():
            st.warning("Please enter your name.")

        elif any(answer is None for answer in answers.values()):
            st.warning("Please answer all questions.")

        else:
            st.session_state.name = name.strip()
            st.session_state.answers = answers
            st.session_state.submitted = True
            st.rerun()

else:

    score, feedback = calculate_score(
        questions,
        st.session_state.answers
    )

    total = len(questions)
    percentage = round((score / total) * 100, 2)

    st.success(f"Congratulations, {st.session_state.name}!")

    st.metric("Your Score", f"{score}/{total}")
    st.metric("Percentage", f"{percentage}%")

    st.progress(percentage / 100)

    if percentage >= 80:
        st.balloons()
        st.success("Excellent Performance!")

    elif percentage >= 50:
        st.info("Good Job! Keep Practicing.")

    else:
        st.warning("Keep Learning and Try Again!")

    if not st.session_state.saved:
        try:
            save_result(
                st.session_state.name,
                score,
                total,
                percentage
            )
            st.session_state.saved = True
            logger.info("Quiz result saved successfully")

        except Exception:
            logger.exception("Database saving failed")
            st.error("Unable to save result.")

    st.subheader("Answer Review")

    for item in feedback:

        with st.expander(
            f"Question {item['number']}"
        ):
            st.write(item["question"])
            st.write(f"Your Answer: {item['selected']}")
            st.write(f"Correct Answer: {item['correct_answer']}")
            st.write(item["explanation"])

    if st.button("Try Again"):
        st.session_state.submitted = False
        st.session_state.saved = False
        st.rerun()

st.divider()

st.subheader("Recent Quiz Results")

try:
    results = get_recent_results()

    if results:
        st.dataframe(results, use_container_width=True)
    else:
        st.info("No quiz results available yet.")

except Exception:
    logger.exception("Unable to retrieve results")
    st.warning("Results are temporarily unavailable.")

st.caption("QuizMaster | Python Capstone Project")
