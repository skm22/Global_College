import streamlit as st

st.title("Student Information Form")

st.header("Registration Form")

name = st.text_input("Enter Name")

age = st.number_input(
    "Enter Age",
    min_value=18,
    max_value=60
)

address = st.text_area("Enter Address")

gender = st.radio(
    "Select Gender",
    ["Male", "Female"]
)

branch = st.selectbox(
    "Select Branch",
    ["CSE", "IT", "AI", "DS"]
)

skills = st.multiselect(
    "Select Skills",
    ["Python", "Java", "SQL", "Machine Learning"]
)

dob = st.date_input("Date of Birth")

interview_time = st.time_input(
    "Preferred Interview Time"
)

rating = st.slider(
    "Rate Your Python Skill",
    1,
    10
)

agree = st.checkbox(
    "I Agree to Terms & Conditions"
)

submit = st.button("Submit")

if submit:

    if agree:

        st.success(
            "Registration Successful"
        )

        st.subheader(
            "Student Details"
        )

        st.write("Name:", name)
        st.write("Age:", age)
        st.write("Address:", address)
        st.write("Gender:", gender)
        st.write("Branch:", branch)
        st.write("Skills:", skills)
        st.write("DOB:", dob)
        st.write(
            "Interview Time:",
            interview_time
        )
        st.write(
            "Python Rating:",
            rating
        )

    else:
        st.error(
            "Please Accept Terms & Conditions"
        )