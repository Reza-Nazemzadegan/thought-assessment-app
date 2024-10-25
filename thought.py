import streamlit as st

# Function to assess thought based on answers
def evaluate_thought(answers):
    positive_responses = sum([1 for answer in answers if answer.lower() in ["yes", "fact", "uplifting", "encouraging"]])
    if positive_responses >= 3:
        return "Mahdis i fekrooo khoobe (Chehreye Reza yadet biad khandan _-(0-o)-_"
    else:
        return "Mahdis i fekrooo khoob nist, yani age 2 daghigheye dg tamomesh nakoni jeret midam :/ "

# Streamlit app layout
st.title("Thought Assessment Tool")
st.write("Write down a thought, and we’ll guide you through questions to see if it’s beneficial or not.")

# Step 1: User writes down their thought
thought = st.text_area("Write your thought here:")

# Step 2: Start questions if the thought is written
if thought:
    st.write("Now, answer these questions to assess your thought.")

    # Initialize a list to hold user responses
    answers = []

    # Question 1
    q1 = st.radio("Does this thought uplift or empower you, or does it bring you down?", ("Uplifting", "Brings me down"))
    answers.append(q1)

    # Question 2
    q2 = st.radio("Is this thought based on facts or assumptions?", ("Fact", "Assumption"))
    answers.append(q2)

    # Question 3
    q3 = st.radio("Does this thought help you achieve your goals or align with your values?", ("Yes", "No"))
    answers.append(q3)

    # Question 4
    q4 = st.radio("How does this thought make you feel emotionally?", ("Positive emotions", "Negative emotions"))
    answers.append(q4)

    # Question 5
    q5 = st.radio("Is this thought encouraging self-compassion or criticism?", ("Encouraging", "Critical"))
    answers.append(q5)

    # Step 3: Evaluate thought based on answers
    if st.button("Evaluate My Thought"):
        result = evaluate_thought(answers)
        st.subheader(result)
