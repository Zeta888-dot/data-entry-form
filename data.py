import streamlit as st
import pandas as pd



st.set_page_config(page_title="Talent Hunt Program Form", layout="wide")


# Create a Streamlit app
st.title("Talent Hunt Program Form - University of Chitral")
st.markdown("This is a data entry form created for the talent hunt program by University of Chitral to help skilled and professional students secure internships in local IT sectors , Banks ." \
"Other than that studets who have business or software ideas are supposed to share with us via the form below. We will be organizing a meeting soon in the supervision of Mr. Masood Anwar SB")

# Define the form fields
with st.form("talent_hunt_form"):
    name = st.text_input("Name")
    age = st.number_input("Age")
    current_semester = st.selectbox("Current Semester", [1, 2, 3, 4, 5, 6, 7, 8])

    # Skills
    skills = st.multiselect("Skills", [
        "Web Development",
        "Data Analysis",
        "Machine Learning",
        "Artificial Intelligence",
        "Cyber Security",
        "Networking",
        "Database Management",
        "Cloud Computing",
        "DevOps",
        "Mobile App Development",
        "Game Development",
        "Other (please specify)"
    ])
    technologies = st.text_input("Technologies e.g HTML,CSS,JS,Python...")

    other_skill = st.text_input("Other Skill (if selected above)")

    # Software ideas
    software_ideas = st.text_area("Software Ideas")

    submit_button = st.form_submit_button("Submit")

# Store the data in a Pandas DataFrame
if submit_button:
    data = {
        "Name": [name],
        "Age": [age],
        "Current Semester": [current_semester],
        "Skills": [", ".join(skills)],
        "Technologies" : technologies,
        "Other Skill": [other_skill],
        "Software Ideas": [software_ideas]
    }
    df = pd.DataFrame(data)

    # Append the data to an existing Excel file or create a new one
    try:
        existing_df = pd.read_csv("talent_hunt_submissions.csv")
        combined_df = pd.concat([existing_df, df])
        combined_df.to_csv("talent_hunt_submissions.csv", index=False)
    except FileNotFoundError:
        df.to_csv("talent_hunt_submissions.csv", index=False)

    st.success("Form submitted successfully!")