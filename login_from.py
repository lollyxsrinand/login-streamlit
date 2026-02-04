import streamlit as st



st.title("Welcome to the Student Management System")

st.header("Anurag University Student Managment Details ")

st.subheader("Manage your student records efficiently")

st.text("This application helps you to add, view, and manage student details seamlessly.")

#Horizontal line
st.markdown("-------------------------------------------------------------------------------------")

st.write("Developed by Anurag University")
st.write([1,2,3,4,5])
st.write({"Name": "Anurag University", "Location": "Hyderabad"})

st.markdown("**BOLD**")

st.markdown("*ITALIC*")
st.markdown("~~STRIKETHROUGH~~")

st.markdown("- item1\n- item 2")

st.markdown("<h3 style='color:red'>Red Text</h3>",unsafe_allow_html=True)

st.caption("This is a caption for the student management system.")

st.code("""
    def add(a,b):
        return a+b
        """, language='python'
)

st.latex(r'''
    E = mc^2
    ''')

st.divider()

if st.button("Click Me"):
    st.write("Button Clicked!")
    st.success("Success Message!")
    st.info("Info Message!")
    st.balloons()
else:
    st.write("U DO One Thing.")
    st.error("Error Message!")


name1 = st.text_input("Enter your name:")
if not name1.isalpha():
    st.error("Please enter a valid name without numbers or special characters.")
else:
    st.write(f"Hello , {name1}!")

feedback = st.text_area("Provide your feedback:")
st.write("Your feedback:", feedback)

if st.checkbox("Subscribe to Newsletter"):
    st.write("Thank you for subscribing!")

st.divider()


gender=st.radio("Choose your Gender:", ["Male", "Female", "Other"])
st.write(f"You selected: {gender}")
st.divider()

datatype = st.selectbox("Select Data Type:", ["Integer", "Float", "String"])
st.write(f"You selected: {datatype}")
st.divider()

hobbies=st.multiselect("Select your Hobbies:", ["Reading", "Traveling", "Gaming", "Cooking"])
st.write("Your hobbies:", hobbies)
st.divider()

age= st.slider("Select your Age:", 0, 100, 25)
st.write(f"You are {age} years old.")
st.divider()



rating= st.select_slider("Rate our Application:", options=[1,2,3,4,5])
st.write(f"You rated us: {rating}")
st.divider()

st.file_uploader("Upload your profile picture:")

st.divider()

with st.form("my form"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, max_value=120)
    submitted = st.form_submit_button("Submit") 

if submitted:
    st.write(f"Form submitted! Name: {name}, Age: {age}")
st.divider()

with st.form("login"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_submitted = st.form_submit_button("Login")   
if login_submitted:
    st.write(f"Login attempted for user: {username}")

st.divider()

col1, col2, col3 = st.columns(3)
with col1:
    st.header("Column 1")
    st.write("descroption 1")

with col2:
    st.header("Column 2")
    st.write("description 2")   

with col3:
    st.header("Column 3")
    st.write("description 3")
st.divider()


container = st.container()
container.write("This is inside the container.")
if container.button("Button"):

    container.write("You clicked the button inside the container!")

st.divider()

data = {
    'Name': ['Anurag', 'Sumit', 'Rohit'],
    'Age': [21, 22, 20],
    'Course': ['B.Tech', 'M.Tech', 'BBA']
}
st.table(data)
st.divider()

st.sidebar.title("sidebar ex")
option = st.sidebar.selectbox("select option",["Home","Dashboard","About Us"])

@st.cache_data
def load_data():
    return [1,2,3,4]

data = load_data()
st.write(data)
