import streamlit as st

st.title("Najiyah's Password Generator")

#All inputs at once
city = st.text_input("Which city did you grow up in?").strip().upper()
city = "".join(city.split())
animal = st.text_input("What is your favorite animal?").strip().lower()
animal = "".join(animal.split())
fav_num = st.text_input("What is your favorite number?")
special_char = st.text_input("Choose ONE special character from these choices: !@#$%^&*",
                             max_chars=1).strip() #Can't use "select" for some reason

#Run the following code if button is clicked
if st.button("Generate Password"):
    valid_flag = True
    if not city.isalpha():
        st.error("Please enter a valid city name with letters and no spaces.")
        valid_flag = False

    if not animal.isalpha():
        st.error("Please enter a valid animal name with letters and no spaces.")
        valid_flag = False

    if not fav_num.isdigit():
        st.error("Invalid input. Enter a positive whole number.")
        valid_flag = False

    allowed_chars = "!@#$%^&*"
    if special_char not in allowed_chars:
        st.error("Please enter ONE valid special character from these choices: !@#$%^&*")
        valid_flag = False

    if valid_flag: # == true is implied
        fav_num = int(fav_num)
        user_password = city[:2] + animal[-2:] + str(fav_num * 2) + len(city) * special_char
        st.success("Your password is generated!")
        st.code(user_password) #allows the user to copy their new password


#py -m streamlit run "[absolute file path]"