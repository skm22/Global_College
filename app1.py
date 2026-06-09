import streamlit as st
# display
st.title("Student Information System")
st.header("Personal Detail")
st.subheader("Enter your Info")
st.write("Welcome to Streamlit")
name = "shailesh"
st.write(name)
st.text("This is the plain text")
st.markdown("# streamlit tutorials")
st.markdown("## streamlit tutorials")
st.markdown("### streamlit tutorials")
st.markdown("**Bold text**")
st.success("registration successfull")

# input 
name=st.text_input("Enter name")
st.write(name)
age= st.number_input("Enter your age",min_value=0, max_value=120, 
                     value=25, step=1)

st.text_area("Enter Address")

# selectBox
branch=st.selectbox(
    "Select Branch ",
    ["CSE","IT","ds","IOT"]
    )

# multiple select option 

skill=st.multiselect(" select skill ",
                     ["python","java","c","c++","SQL","ml"])
gender=st.radio("Gender",["male","female"])
agree=st.checkbox("I agree to term and conditions ")
date=st.date_input("Enter the date")
time=st.time_input("Enter the time ")
rate=st.slider("Rate Your python skill",1,10)

id=st.text_input("Enter your id ")
if not id:
    st.warning("Please enter your id ")

# button=st.button("Submit")
if st.button("Submit"):
    st.success("form submitted successfully")
