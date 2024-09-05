import streamlit as st


st.title("Demo AI learning")
st.header("Heading of Streamlit")
st.subheader("this is a sub heading")
st.text("This is a text")
st.success("Sucess")
st.warning("warning")
st.info("Info")
st.error("Error")
if st.checkbox("Select/Unselect"):
    st.text("User selected the checkbox")
else:
    st.text("User did not select")

state = st.radio("what is your favourite Color ?", ("Red", "Green", "yellow"))

if state == "Green":
    st.success("Thats my favourite colour as well")


occupation = st.selectbox("What do you do for a living",["Student", "Vlogger", "Engineer"])

st.text(f"selected option is {occupation}")
if st.button("Example Button"):
    st.error("You clicked it ")


st.sidebar.header("Heading of sidebar")
st.sidebar.text("Created a side Bar")